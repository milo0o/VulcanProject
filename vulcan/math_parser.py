import math

class MathEvaluator:
    def __init__(self):
        self.env = {
            "pi": math.pi, "e": math.e, "phi": (1.0 + math.sqrt(5.0)) / 2.0,
            "c": 299792458.0, "g_earth": 9.80665, "big_g": 6.67430e-11,
            "h": 6.62607015e-34, "hbar": 1.0545718e-34, "m_e": 9.1093837e-31, "m_p": 1.6726219e-27,
            "q": 1.602176634e-19, "eps_0": 8.8541878e-12, "mu_0": 1.25663706e-6, "k_b": 1.380649e-23,
            "alpha": 1/137.035999,
            "sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt, "log": math.log, "exp": math.exp
        }

    def evaluate(self, expr):
        clean_expr = str(expr).replace('^', '**')
        try:
            return eval(clean_expr, {"__builtins__": None}, self.env)
        except Exception as e:
            raise ValueError(f"Invalid Math Expression. {e}")
