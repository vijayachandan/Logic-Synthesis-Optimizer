# draw_circuit.py
from graphviz import Digraph
from simple_netlist import generate_netlist

def draw_gate_diagram(expr):
    """
    Streamlit-safe gate diagram generator.
    Returns a Graphviz Digraph (NO .render()).
    """

    netlist = generate_netlist(expr)

    dot = Digraph()
    dot.attr(rankdir="LR")

    for gate, inputs in netlist.items():
        gate_type = gate.split("_")[0]

        if gate_type == "AND":
            dot.node(gate, "AND", shape="box")
        elif gate_type == "OR":
            dot.node(gate, "OR", shape="box")
        elif gate_type == "NOT":
            dot.node(gate, "NOT", shape="box")
        else:
            dot.node(gate, gate)

        for inp in inputs:
            dot.edge(inp, gate)

    return dot
