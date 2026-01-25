# app.py
# Logic Synthesis Optimizer — UI POLISH STEP 1 (Visual Refinement)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
from sympy.parsing.sympy_parser import parse_expr

from expression_pipeline import run_expression_pipeline
from truth_table_to_expr import truth_table_to_sop
from draw_circuit import draw_gate_diagram

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Logic Synthesis Optimizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# UI POLISH STEP 1 — CSS
# --------------------------------------------------
st.markdown("""
<style>

/* Base */
html, body {
    background-color: #0b1220;
}
.block-container {
    padding-top: 1.8rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
}

/* Typography */
h1 {
    font-size: 2.4rem;
    font-weight: 800;
}
h2 {
    font-size: 1.6rem;
    font-weight: 700;
}
h3 {
    font-size: 1.25rem;
    font-weight: 650;
}
p {
    color: #cbd5e1;
}

/* Cards */
.card {
    background-color: #020617;
    padding: 22px 26px;
    border-radius: 16px;
    border: 1px solid #1e293b;
    margin-bottom: 22px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
}

/* Highlight card */
.highlight {
    border: 2px solid #22c55e;
    box-shadow: 0 0 14px rgba(34,197,94,0.35);
}

/* Badge */
.badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-top: 6px;
}
.badge-selected {
    background-color: #22c55e;
    color: #052e16;
}

/* Sidebar */
.css-1d391kg {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

/* Tabs spacing */
.stTabs [data-baseweb="tab"] {
    font-size: 15px;
    padding: 10px 18px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("""
<div class="card">
  <h1>🧠 Logic Synthesis Optimizer</h1>
  <p>
    Truth Table → Canonical SOP → Multiple Implementations → AI-Based Selection → Hardware Output
  </p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR — INPUT CONTROL
# ==================================================
st.sidebar.header("⚙ Input Configuration")

input_type = st.sidebar.selectbox(
    "Select Input Type",
    ["Boolean Expression", "Truth Table", "Gate-Level Circuit"]
)

expr_input = None
truth_table_input = None
gate_input = None

if input_type == "Boolean Expression":
    expr_input = st.sidebar.text_area(
        "Boolean Expression",
        height=120,
        placeholder="((A & B) & (A | B)) | ((A | C) & (A | D))"
    )

elif input_type == "Truth Table":
    num_vars = st.sidebar.selectbox("Number of Variables", [2, 3, 4])
    rows = 2 ** num_vars
    truth_table_input = []

    st.sidebar.markdown("Fill output **F** values:")

    for i in range(rows):
        bits = list(map(int, format(i, f"0{num_vars}b")))
        f_val = st.sidebar.toggle(
            f"{''.join(map(str, bits))} → F",
            key=f"tt_{i}"
        )
        truth_table_input.append(tuple(bits + [int(f_val)]))

else:
    gate_input = st.sidebar.text_area(
        "Gate-Level Netlist",
        height=150,
        placeholder="G1 = AND(A, B)\nG2 = NOT(C)\nF = OR(G1, G2)"
    )

run = st.sidebar.button("🚀 Run Synthesis")

# ==================================================
# BACKEND EXECUTION
# ==================================================
result = None

if run:
    with st.spinner("Running logic synthesis..."):
        time.sleep(0.4)

        if input_type == "Boolean Expression":
            result = run_expression_pipeline(expr_input)

        elif input_type == "Truth Table":
            expr = truth_table_to_sop(truth_table_input)
            result = run_expression_pipeline(expr)

        else:
            gate_map = {}
            for line in gate_input.splitlines():
                if "=" not in line:
                    continue
                lhs, rhs = line.split("=")
                lhs = lhs.strip()
                rhs = rhs.strip()

                if rhs.startswith("AND"):
                    a, b = rhs[4:-1].split(",")
                    gate_map[lhs] = parse_expr(a.strip(), gate_map) & parse_expr(b.strip(), gate_map)
                elif rhs.startswith("OR"):
                    a, b = rhs[3:-1].split(",")
                    gate_map[lhs] = parse_expr(a.strip(), gate_map) | parse_expr(b.strip(), gate_map)
                elif rhs.startswith("NOT"):
                    a = rhs[4:-1]
                    gate_map[lhs] = ~parse_expr(a.strip(), gate_map)

            result = run_expression_pipeline(str(gate_map["F"]))

# ==================================================
# RESULTS VIEW
# ==================================================
if result:
    # Canonical SOP
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📘 Canonical SOP (Truth-Table Derived)")
    with st.expander("Show canonical expression"):
        st.code(result["expression"])
    st.markdown('</div>', unsafe_allow_html=True)

    # Implementations table
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧩 Generated Implementations")

    rows = []
    for impl in result["implementations"]:
        rows.append({
            "Implementation": impl["name"],
            "Expression": impl["expression"],
            "Depth": impl["logic_depth"],
            "Cost": impl["cost"],
            "Selected": "✅" if impl["name"] == result["best_version"] else ""
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # AI Decision
    st.markdown('<div class="card highlight">', unsafe_allow_html=True)
    st.markdown("### 🤖 AI-Selected Implementation")
    st.markdown(f"""
**Expression:**  
`{result["optimized_expression"]}`  

<div class="badge badge-selected">Selected</div>  
**Total Cost:** `{result["cost"]}`
""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Output Tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📐 Gate Diagram", "📈 Waveforms", "📊 Truth Table", "💻 Verilog HDL"]
    )

    with tab1:
        diagram = draw_gate_diagram(result["optimized_expression"])
        st.graphviz_chart(diagram)


    with tab2:
        tt_df = pd.DataFrame(
            result["truth_table"],
            columns=result["variables"] + ["F"]
        )

        fig, axes = plt.subplots(len(tt_df.columns), 1, figsize=(12, 2 * len(tt_df.columns)), sharex=True)
        t = range(len(tt_df))

        for i, col in enumerate(tt_df.columns):
            axes[i].step(t, tt_df[col], where="post")
            axes[i].set_ylabel(col)
            axes[i].grid(True)

        st.pyplot(fig)

    with tab3:
        st.dataframe(tt_df, use_container_width=True)

    with tab4:
        st.code(result["verilog"], language="verilog")
        st.download_button(
            "⬇ Download Verilog",
            result["verilog"],
            "optimized_logic.v"
        )
