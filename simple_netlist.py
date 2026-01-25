# simple_netlist.py
# Generates a simple gate-level netlist (DICT FORMAT)

from sympy.parsing.sympy_parser import parse_expr
from sympy.logic.boolalg import And, Or, Not

def generate_netlist(expr_str):
    """
    Generate a gate-level netlist as a dictionary:
    gate_name -> list of input signals
    """

    expr = parse_expr(expr_str)
    netlist = {}
    counter = {"G": 0}

    def new_gate():
        counter["G"] += 1
        return f"G{counter['G']}"

    def walk(node):
        # Variable
        if node.is_Atom:
            return str(node)

        # NOT
        if isinstance(node, Not):
            inp = walk(node.args[0])
            g = new_gate()
            netlist[g] = [inp]
            return g

        # AND / OR
        if isinstance(node, (And, Or)):
            inputs = [walk(arg) for arg in node.args]
            g = new_gate()
            netlist[g] = inputs
            return g

        return str(node)

    output_gate = walk(expr)
    netlist["F"] = [output_gate]

    return netlist
