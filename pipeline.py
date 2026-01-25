# pipeline.py — FINAL CLEAN VERSION

from truth_table_to_expr import truth_table_to_sop
from ai_selector import select_best_version
from final_verilog import generate_verilog


def run_pipeline():
    truth_table = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ]

    expr = truth_table_to_sop(truth_table)
    name, best_expr, cost = select_best_version(expr)
    verilog_code = generate_verilog(best_expr)

    return {
        "truth_table": truth_table,
        "expression": expr,
        "best_version": name,
        "optimized_expression": best_expr,
        "cost": round(cost, 2),
        "verilog": verilog_code
    }
