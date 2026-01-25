# expression_pipeline.py
# STEP 4: AI-based selection of best gate-level implementation

from sympy.logic.boolalg import simplify_logic, Not, And
from sympy.parsing.sympy_parser import parse_expr

from expression_to_truth_table import expression_to_truth_table
from truth_table_to_expr import truth_table_to_sop
from gate_counter import count_gates
from logic_depth import calculate_depth
from final_verilog import generate_verilog

from nand_mapper import to_nand
from nor_mapper import to_nor
from ai_selector import select_best_implementation


def generate_implementations(expr_str):
    implementations = []

    parsed = parse_expr(expr_str)

    # Canonical SOP
    implementations.append({
        "name": "Canonical SOP",
        "expression": expr_str,
        "gate_count": count_gates(expr_str),
        "logic_depth": calculate_depth(expr_str)
    })

    # DeMorgan
    if len(parsed.args) <= 1:
        demorgan_expr = parsed
    else:
        demorgan_expr = Not(
            And(*[Not(arg) for arg in parsed.args])
        )

    demorgan_str = str(demorgan_expr)

    implementations.append({
        "name": "DeMorgan Form",
        "expression": demorgan_str,
        "gate_count": count_gates(demorgan_str),
        "logic_depth": calculate_depth(demorgan_str)
    })

    # NAND-only
    nand_expr = to_nand(parsed)
    nand_str = str(nand_expr)

    implementations.append({
        "name": "NAND-only",
        "expression": nand_str,
        "gate_count": count_gates(nand_str),
        "logic_depth": calculate_depth(nand_str)
    })

    # NOR-only
    nor_expr = to_nor(parsed)
    nor_str = str(nor_expr)

    implementations.append({
        "name": "NOR-only",
        "expression": nor_str,
        "gate_count": count_gates(nor_str),
        "logic_depth": calculate_depth(nor_str)
    })

    return implementations


def run_expression_pipeline(expr_str):
    # 1️⃣ Truth table (ground truth)
    var_names, truth_table = expression_to_truth_table(expr_str)

    # 2️⃣ Canonical SOP
    sop_expr = truth_table_to_sop(truth_table)
    simplified = simplify_logic(sop_expr, form="dnf")
    simplified_str = str(simplified)

    # 3️⃣ Generate implementations
    implementations = generate_implementations(simplified_str)

    # 4️⃣ AI selection
    best_impl, ranked_impls = select_best_implementation(implementations)

    # 5️⃣ Verilog
    verilog = generate_verilog(best_impl["expression"])

    return {
        "truth_table": truth_table,
        "variables": var_names,
        "expression": sop_expr,
        "optimized_expression": best_impl["expression"],
        "implementations": ranked_impls,   # ranked by cost
        "best_version": best_impl["name"],
        "cost": best_impl["cost"],
        "verilog": verilog
    }
