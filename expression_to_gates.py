# expression_to_gates.py

def extract_gates(expr):
    gates = {
        "AND": expr.count('&'),
        "OR": expr.count('|'),
        "NOT": expr.count('~')
    }
    return gates


# ---------- TEST ----------
if __name__ == "__main__":
    expr = "(A & B) | (~A & C)"
    gates = extract_gates(expr)

    print("Expression:", expr)
    print("Gate Usage:")
    for gate, count in gates.items():
        print(f"{gate}: {count}")

