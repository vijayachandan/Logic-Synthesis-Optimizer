# 🧠 Logic Synthesis Optimizer

An AI-assisted VLSI logic synthesis tool that converts Boolean logic specifications into optimized hardware implementations with gate-level visualization and Verilog HDL generation.

---

## 🚀 Features

- Accepts **Boolean Expression**, **Truth Table**, or **Gate-Level** input
- Generates **Canonical SOP** (truth-table exact)
- Performs **Boolean minimization**
- Creates multiple **logic implementations**:
  - Simplified (Base)
  - DeMorgan form
  - NAND-only
  - NOR-only
- Uses **AI-based cost evaluation** to select the optimal implementation
- Visualizes:
  - Gate-level circuit diagram
  - Timing waveforms
  - Truth table
- Generates **synthesizable Verilog HDL**
- Interactive **Streamlit web interface**

---

## 🧠 AI-Based Optimization

Each implementation is evaluated using a cost function based on:
- Gate count
- Logic depth
- Structural complexity

The AI selects the implementation with the lowest overall cost, simulating real-world synthesis trade-offs.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Web UI)
- **SymPy** (Boolean logic processing)
- **Graphviz** (Gate-level diagrams)
- **Matplotlib** (Waveforms)
- **Scikit-learn** (Cost modeling)

---

- Main UI  
- Generated implementations  
- Gate-level diagram  
- Verilog output  

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/logic-synthesis-optimizer.git
cd logic-synthesis-optimizer
pip install -r requirements.txt
streamlit run app.py
