# cost_function.py

from feature_extractor import extract_features

def calculate_cost(expr):
    features = extract_features(expr)

    total_gates = features[0]
    depth = features[1]

    cost = total_gates + 2 * depth
    return cost


# ---------- TEST ----------
if __name__ == "__main__":
    user_input = "(A & B) | (~A & C)"
    print("Cost:", calculate_cost(user_input))
