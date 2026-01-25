# expression_to_truth_table.py
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

def expression_to_truth_table(expr_str):
    """
    Converts a Boolean expression to a full truth table.
    Returns: (variables, table)
    table rows: (x1, x2, ..., xN, F)
    """

    # Detect variables dynamically
    var_names = sorted(set(c for c in expr_str if c.isalpha()))
    vars = symbols(" ".join(var_names))

    expr = parse_expr(expr_str, local_dict=dict(zip(var_names, vars)))

    table = []
    num_vars = len(vars)

    for i in range(2 ** num_vars):
        values = list(map(int, format(i, f"0{num_vars}b")))
        env = dict(zip(vars, values))
        output = int(bool(expr.subs(env)))
        table.append(tuple(values + [output]))

    return var_names, table
