# draw_circuit.py
# Draws a gate-level circuit diagram from a DICT netlist

from graphviz import Digraph
from simple_netlist import generate_netlist


def draw_gate_diagram(expr_str, output_name="gate_level_circuit"):
    """
    Draw gate-level circuit and return PNG path.
    """

    netlist = generate_netlist(expr_str)

    dot = Digraph(format="png")
    dot.attr(rankdir="LR")

    # Draw nodes
    for gate in netlist:
        shape = "oval" if gate == "F" else "box"
        dot.node(gate, gate, shape=shape)

    # Draw edges
    for gate, inputs in netlist.items():
        for inp in inputs:
            dot.edge(inp, gate)

    path = dot.render(output_name, cleanup=True)
    return path
