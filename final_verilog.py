# final_verilog.py
# Pure Verilog generator (NO AI logic here)

def generate_verilog(expr_str):
    """
    Generate Verilog code from a Boolean expression string.
    """

    # Extract variable names (A, B, C, ...)
    variables = sorted(set(c for c in expr_str if c.isalpha()))

    inputs = ",\n    ".join(f"input {v}" for v in variables)

    verilog = f"""
module optimized_logic(
    {inputs},
    output F
);
    assign F = {expr_str};
endmodule
"""

    return verilog
