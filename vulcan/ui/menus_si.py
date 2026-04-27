import math
from vulcan.ui.header import clear_screen, print_header, print_triad, Color

def menu_si_conversions(flow, parser):
    while True:
        clear_screen()
        print_header()
        print(f"{Color.CYAN}--- MODULE 2: SI DIMENSIONAL TRANSMUTATION ---{Color.RESET}")
        print(f"{Color.GREEN} [1]{Color.RESET} Energy (Joules to Electron-Volts)")
        print(f"{Color.GREEN} [2]{Color.RESET} Length (Meters to Planck Lengths)")
        print(f"{Color.GREEN} [3]{Color.RESET} Mass (Kg to eV/c^2)")
        print(f"{Color.RED} [0]{Color.RESET} Return to Main Menu\n")

        choice = input(f"{Color.YELLOW}>> Select Conversion: {Color.RESET}")
        if choice == '0': break
        try:
            if choice == '1':
                val = parser.evaluate(input(f"{Color.YELLOW}>> Input Joules: {Color.RESET}"))
                print_triad(flow, "ELECTRON-VOLTS (eV)", val / parser.env["q"])
            elif choice == '2':
                val = parser.evaluate(input(f"{Color.YELLOW}>> Input Meters: {Color.RESET}"))
                l_p = math.sqrt((parser.env["hbar"] * parser.env["big_g"]) / (parser.env["c"]**3))
                print_triad(flow, "PLANCK LENGTHS", val / l_p)
            elif choice == '3':
                val = parser.evaluate(input(f"{Color.YELLOW}>> Input Kilograms: {Color.RESET}"))
                print_triad(flow, "MASS (eV/c^2)", val * 5.609588e35)
        except Exception as e:
            print(f"{Color.RED}[!] Error: {e}{Color.RESET}")
        input(f"{Color.CYAN}Press Enter to continue...{Color.RESET}")
