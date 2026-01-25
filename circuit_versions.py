# circuit_versions.py

def generate_versions(expr):
    versions = {}

    # Version 1: original
    versions["Original"] = expr

    # Version 2: extra brackets (same logic, different structure)
    versions["Bracketed"] = f"(({expr}))"

    # Version 3: reordered terms (manual, simple)
    versions["Reordered"] = "(~A & C) | (A & B)"

    return versions


# ---------- TEST ----------
if __name__ == "__main__":
    expr = "(A & B) | (~A & C)"
    versions = generate_versions(expr)

    for name, v in versions.items():
        print(name, ":", v)
