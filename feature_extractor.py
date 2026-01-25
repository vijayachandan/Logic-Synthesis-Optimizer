# feature_extractor.py

from gate_counter import count_gates
from logic_depth import calculate_depth

def extract_features(expr_str):
    """
    Feature vector for AI cost model
    """

    gates = count_gates(expr_str)
    depth = calculate_depth(expr_str)

    return {
        "and_count": gates.get("AND", 0),
        "or_count": gates.get("OR", 0),
        "not_count": gates.get("NOT", 0),
        "logic_depth": depth
    }
