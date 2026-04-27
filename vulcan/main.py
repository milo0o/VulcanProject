import time

# Computation Imports
from vulcan.flow_system import FlowSystem
from vulcan.math_parser import MathEvaluator

# UI Imports
from vulcan.ui.header import clear_screen, print_header, Color
from vulcan.ui.menus_general_math import menu_general_math
from vulcan.ui.menus_si import menu_si_conversions
from vulcan.ui.menus_evanescent import menu_evanescent_light
from vulcan.ui.menus_periodic import menu_periodic_table
from vulcan.ui.menus_codex import menu_codex

def main():
    flow = FlowSystem()
    parser = MathEvaluator()

    while True:
        clear_screen()
        print_header()
        print(f"{Color.GREEN} [1]{Color.RESET} General Mathematics (Etheric Computation)")
        print(f"{Color.GREEN} [2]{Color.RESET} SI Dimensional Transmutation (Unit Conversions)")
        print(f"{Color.GREEN} [3]{Color.RESET} Evanescent Light & Gravity Mechanics")
        print(f"{Color.GREEN} [4]{Color.RESET} The Alchemical Periodic Table (1-118 Restored)")
        print(f"{Color.MAGENTA} [5]{Color.RESET} The Vulcan Codex (Master Schematics & Hypotheses)")
        print(f"{Color.RED} [0]{Color.RESET} Power Down Mainframe\n")

        choice = input(f"{Color.YELLOW}>> Awaiting Sequence: {Color.RESET}")

        if choice == '0':
            print(f"\n{Color.MAGENTA}[!] Securing etheric circuits. Shutting down...{Color.RESET}")
            break
        elif choice == '1': 
            menu_general_math(flow, parser)
        elif choice == '2': 
            menu_si_conversions(flow, parser)
        elif choice == '3': 
            menu_evanescent_light(flow, parser)
        elif choice == '4': 
            menu_periodic_table(flow)
        elif choice == '5': 
            menu_codex()
        else:
            print(f"{Color.RED}[!] Invalid sequence. Recalibrate.{Color.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
