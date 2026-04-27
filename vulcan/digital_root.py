def get_dr_base10(n):
    if abs(n) < 1e-45: return "0"
    s = f"{abs(n):.15e}"
    mantissa = s.split('e')[0]
    digits = [int(c) for c in mantissa if c.isdigit() and c != '0']
    if not digits: return "9"
    total = sum(digits)
    while total > 9:
        total = sum(int(c) for c in str(total))
    return str(total)

def get_dr_flow(s):
    digits = [int(c) for c in str(s) if c.isdigit()]
    if not digits: return "0"
    total = sum(digits)
    while total > 9:
        total = sum(int(c) for c in str(total))
    return str(total)
