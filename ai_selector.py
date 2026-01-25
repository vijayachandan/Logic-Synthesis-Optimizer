# ai_selector.py
# AI-based implementation selector (cost-driven)

def compute_cost(impl):
    """
    Compute cost of an implementation based on hardware metrics.
    """

    gates = impl["gate_count"]
    depth = impl["logic_depth"]

    cost = (
        gates.get("AND", 0) * 1.0 +
        gates.get("OR", 0)  * 1.0 +
        gates.get("NOT", 0) * 0.5 +
        depth * 2.0
    )

    return cost


def select_best_implementation(implementations):
    """
    Select the best implementation based on cost.
    """

    scored = []

    for impl in implementations:
        cost = compute_cost(impl)
        impl_with_cost = impl.copy()
        impl_with_cost["cost"] = round(cost, 2)
        scored.append(impl_with_cost)

    # Sort by cost (ascending)
    scored.sort(key=lambda x: x["cost"])

    best = scored[0]

    return best, scored
