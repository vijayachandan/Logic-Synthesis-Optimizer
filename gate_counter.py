# gate_counter.py

def count_gates(expr):
    and_count = expr.count('&')
    or_count = expr.count('|')
    not_count = expr.count('~')

    total_gates = and_count + or_count + not_count

    return {
        "AND": and_count,
        "OR": or_count,
        "NOT": not_count,
        "TOTAL": total_gates
    }


# ---------- TEST ----------
if __name__ == "__main__":
    user_input = "(A & B) | (~A & C)"
    counts = count_gates(user_input)

    print("Gate Count:")
    for gate, count in counts.items():
        print(f"{gate}: {count}")
