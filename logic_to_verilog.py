# logic_to_verilog.py

def logic_to_verilog(expr):
    verilog_code = f"""
module logic_module(
    input A,
    input B,
    input C,
    output F
);
    assign F = {expr};
endmodule
"""
    return verilog_code


# ---------- TEST ----------
if __name__ == "__main__":
    user_input = "(A & B) | (~A & C)"
    print(logic_to_verilog(user_input))
