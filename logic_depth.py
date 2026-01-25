# logic_depth.py
# Single-source logic depth calculator
# NO imports from project files (IMPORTANT)

from sympy.parsing.sympy_parser import parse_expr

def calculate_depth(expr_str):
    """
    Calculates logic depth of a Boolean expression.
    Each logic operator adds one level.
    """

    expr = parse_expr(expr_str)

    def depth(node):
        # Leaf node (variable or constant)
        if not hasattr(node, "args") or len(node.args) == 0:
            return 0
        return 1 + max(depth(arg) for arg in node.args)

    return depth(expr)
