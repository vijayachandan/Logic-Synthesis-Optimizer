# nor_mapper.py
# Converts a Boolean expression into NOR-only form

from sympy.parsing.sympy_parser import parse_expr
from sympy.logic.boolalg import And, Or, Not

def to_nor(expr):
    """
    Recursively convert expression to NOR-only form.
    Returns a SymPy expression.
    """

    # Variable
    if expr.is_Atom:
        return expr

    # NOT
    if isinstance(expr, Not):
        a = to_nor(expr.args[0])
        return ~(a | a)   # NOR(a, a)

    # OR
    if isinstance(expr, Or):
        a = to_nor(expr.args[0])
        b = to_nor(expr.args[1])
        t = ~(a | b)      # NOR(a, b)
        return ~(t | t)   # NOT(NOR)

    # AND
    if isinstance(expr, And):
        a = to_nor(expr.args[0])
        b = to_nor(expr.args[1])
        na = ~(a | a)     # NOT(a)
        nb = ~(b | b)     # NOT(b)
        return ~(na | nb) # NOR(na, nb)

    return expr
