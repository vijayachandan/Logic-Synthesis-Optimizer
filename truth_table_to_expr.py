# truth_table_to_expr.py
from sympy import symbols
from sympy.logic.boolalg import And, Or, Not

def truth_table_to_sop(table):
    """
    Canonical SOP generator.
    Table format: [(A, B, C, ..., F), ...]
    """

    num_vars = len(table[0]) - 1
    var_names = [chr(ord('A') + i) for i in range(num_vars)]
    vars = symbols(" ".join(var_names))

    minterms = []

    for row in table:
        *inputs, output = row
        if output == 1:
            terms = []
            for val, var in zip(inputs, vars):
                terms.append(var if val else Not(var))
            minterms.append(And(*terms))

    if not minterms:
        return "0"

    return str(Or(*minterms))
