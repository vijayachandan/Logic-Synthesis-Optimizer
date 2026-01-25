# expression_validator.py

import re

def is_valid_expression(expr):
    expr = expr.strip()

    if not expr:
        return False, "Expression cannot be empty."

    # ❌ Reject C-style logical operators
    if "&&" in expr or "||" in expr:
        return False, "Use '&' for AND and '|' for OR (not && or ||)."

    # Allowed characters only
    pattern = r'^[A-Za-z0-9\s&|~()]+$'
    if not re.match(pattern, expr):
        return False, "Expression contains invalid characters."

    # Parentheses balance check
    stack = []
    for ch in expr:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False, "Unbalanced parentheses."
            stack.pop()

    if stack:
        return False, "Unbalanced parentheses."

    return True, ""
