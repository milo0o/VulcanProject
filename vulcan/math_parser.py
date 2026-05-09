import math

class MathEvaluator:
    def __init__(self):
        # The cosmological environment and topological operators
        self.env = {
            "pi": math.pi, "e": math.e, "phi": (1.0 + math.sqrt(5.0)) / 2.0,
            "c": 299792458.0, "g_earth": 9.80665, "big_g": 6.67430e-11,
            "h": 6.62607015e-34, "hbar": 1.0545718e-34, "m_e": 9.1093837e-31, "m_p": 1.6726219e-27,
            "q": 1.602176634e-19, "eps_0": 8.8541878e-12, "mu_0": 1.25663706e-6, "k_b": 1.380649e-23,
            "alpha": 1/137.035999,
            
            # The 3D Firmament Generators
            "sin": math.sin, "cos": math.cos, "tan": math.tan, 
            
            # The 4D w-axis Retroactive Collapse Operators
            "arcsin": math.asin, "arccos": math.acos, "arctan": math.atan, 
            
            # Continuous Flow Metrics
            "sqrt": math.sqrt, "log": math.log, "log10": math.log10, "exp": math.exp,
            "deg": math.degrees, "rad": math.radians
        }

    def evaluate(self, expr):
        # Sanitize the string
        clean_expr = str(expr).replace('^', '**')
        
        # --- DIAGNOSTIC HUD ---
        print(f"\n[SYSTEM DEBUG] Raw Input: {repr(expr)}")
        print(f"[SYSTEM DEBUG] Cleaned Expr: {repr(clean_expr)}")
        # ----------------------
        
        try:
            return eval(clean_expr, {"__builtins__": None}, self.env)
        except Exception as e:
            # We want the exact Python exception type and message
            raise ValueError(f"\n[!] Core Fault. \nExpression: '{clean_expr}' \nExact Error: {type(e).__name__} - {e}")
