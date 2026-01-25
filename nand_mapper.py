# nand_mapper.py
# Converts a Boolean expression into NAND-only form

from sympy.parsing.sympy_parser import parse_expr
from sympy.logic.boolalg import And, Or, Not

def to_nand(expr):
    """
    Recursively convert expression to NAND-only form.
    Returns a SymPy expression.
    """

    # Variable
    if expr.is_Atom:
        return expr

    # NOT
    if isinstance(expr, Not):
        a = to_nand(expr.args[0])
        return ~(a & a)   # NAND(a, a)

    # AND
    if isinstance(expr, And):
        a = to_nand(expr.args[0])
        b = to_nand(expr.args[1])
        t = ~(a & b)      # NAND(a, b)
        return ~(t & t)   # NOT(NAND)

    # OR
    if isinstance(expr, Or):
        a = to_nand(expr.args[0])
        b = to_nand(expr.args[1])
        na = ~(a & a)     # NOT(a)
        nb = ~(b & b)     # NOT(b)
        return ~(na & nb) # NAND(na, nb)

    # Fallback
    return expr
