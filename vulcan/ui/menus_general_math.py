from vulcan.ui.header import clear_screen, print_header, print_triad, Color

def menu_general_math(flow, parser):
    while True:
        clear_screen()
        print_header()
        print(f"{Color.CYAN}--- MODULE 1: GENERAL MATHEMATICS ---{Color.RESET}")
        print("Variables enabled: pi, e, phi, c, h, hbar, m_e, m_p, q, eps_0, mu_0, big_g, g_earth, alpha")
        print("Type 'back' to return.")
        expr = input(f"{Color.YELLOW}>> Input Base 10 Math Expression: {Color.RESET}")
        if expr.lower() == 'back': break
        try:
            val = parser.evaluate(expr)
            print_triad(flow, "COMPUTATION", val)
        except Exception as e:
            print(f"{Color.RED}[!] Error: {e}{Color.RESET}")
        input(f"{Color.CYAN}Press Enter to continue...{Color.RESET}")
