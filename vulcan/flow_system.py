import math

class FlowSystem:
    def __init__(self):
        self.PI = math.pi
        self.base = round(math.hypot(9.0 * math.cos(self.PI), 9.0 * math.sin(self.PI)))
        self.offset = round(math.sin(self.PI / 4.0)**2 + math.cos(self.PI / 4.0)**2)
        self.ascii_zero = round(96.0 * math.sin(self.PI / 6.0))

    def propagate_integer(self, n):
        if n == 0: return "0"
        current = int(n)
        digits = []
        while current > 0:
            current -= self.offset
            digits.append((current % self.base) + self.offset)
            current //= self.base
        return "".join(chr(self.ascii_zero + d) for d in reversed(digits))

    def propagate_decimal(self, frac):
        if frac == 0.0: return ""
        precision = 12
        digits = []
        m = frac
        for _ in range(precision):
            m *= self.base
            d = math.floor(m)
            digits.append(d)
            m -= d
        for i in range(precision - 1, 0, -1):
            if digits[i] <= 0:
                digits[i - 1] -= 1
                digits[i] += 9
        result = "."
        sig = False
        for d in digits:
            if d > 0: sig = True
            if not sig and d <= 0: result += "0"
            else: result += chr(self.ascii_zero + (9 if d <= 0 else d))
        return result

    def convert_scientific(self, n):
        e = math.floor(math.log(n, 9.0))
        m = n / (9.0 ** e)
        if m >= 9.0: m /= 9.0; e += 1
        if m < 1.0: m *= 9.0; e -= 1

        digits = []
        for _ in range(12):
            d = math.floor(m)
            digits.append(d)
            m = (m - d) * 9.0

        for i in range(11, 0, -1):
            if digits[i] <= 0:
                digits[i - 1] -= 1
                digits[i] += 9
        while digits and digits[0] <= 0:
            digits.pop(0); e -= 1; digits.append(9)

        result = chr(self.ascii_zero + digits[0]) + "."
        for d in digits[1:]:
            result += chr(self.ascii_zero + (9 if d <= 0 else d))

        exp_str = f"-{self.propagate_integer(-e)}" if e < 0 else (self.propagate_integer(e) if e > 0 else "0")
        return f"{result} * 9^{exp_str}"

    def convert(self, n):
        if abs(n) < 1e-45: return "0 (The Fulcrum)"
        polarity = "-" if n < 0 else ""
        abs_n = abs(n)
        if abs_n >= 1e11 or (0 < abs_n < 1e-4): return polarity + self.convert_scientific(abs_n)
        int_part = math.floor(abs_n)
        frac_part = abs_n - int_part
        int_str = "0" if int_part == 0 else self.propagate_integer(int_part)
        return polarity + int_str + self.propagate_decimal(frac_part)
