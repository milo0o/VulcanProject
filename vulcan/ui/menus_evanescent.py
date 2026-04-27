import math
from vulcan.ui.header import clear_screen, print_header, print_triad, Color
from vulcan.interaction_geometry.visualizer import plot_evanescent_wave

def menu_evanescent_light(flow, parser):
    while True:
        clear_screen()
        print_header()
        print(f"{Color.CYAN}--- MODULE 3: EVANESCENT LIGHT & GRAVITY ---{Color.RESET}")
        print(f"{Color.GREEN} [1]{Color.RESET} The Weight of Light (Pair Production Metric)")
        print(f"{Color.GREEN} [2]{Color.RESET} Dynamic Gravity Solver (Integrate Local G)")
        print(f"{Color.GREEN} [3]{Color.RESET} Reverse Lightning Strike (Quantum Buoyancy)")
        print(f"{Color.GREEN} [4]{Color.RESET} LC Circuit Etheric Resonance")
        print(f"{Color.GREEN} [5]{Color.RESET} VISUALIZER: Graph Evanescent Phase Shift")
        print(f"{Color.RED} [0]{Color.RESET} Return to Main Menu\n")

        choice = input(f"{Color.YELLOW}>> Select Operation: {Color.RESET}")
        if choice == '0': break
        try:
            h = parser.env["h"]; c = parser.env["c"]; pi = parser.env["pi"]
            if choice == '1':
                f = parser.evaluate(input(f"{Color.YELLOW}>> Input Light Freq [Hz]: {Color.RESET}"))
                g = parser.evaluate(input(f"{Color.YELLOW}>> Input Local G [m/s^2]: {Color.RESET}"))
                print_triad(flow, "KINETIC WEIGHT (kg)", ((h * f) / (c**2)) * g)
            elif choice == '2':
                W = parser.evaluate(input(f"{Color.YELLOW}>> Input Observed Weight Drag [kg]: {Color.RESET}"))
                f = parser.evaluate(input(f"{Color.YELLOW}>> Input Reference Freq [Hz]: {Color.RESET}"))
                print_triad(flow, "DYNAMIC GRAVITY (G)", (W * (c**2)) / (h * f))
            elif choice == '3':
                f = parser.evaluate(input(f"{Color.YELLOW}>> Input Photon Freq [Hz]: {Color.RESET}"))
                rho = parser.evaluate(input(f"{Color.YELLOW}>> Input Local Vacuum Density (rho_psi): {Color.RESET}"))
                g = parser.evaluate(input(f"{Color.YELLOW}>> Input Local G [m/s^2]: {Color.RESET}"))
                V_photon = (pi * (c**3)) / (6 * (f**3))
                W_light = (h * f) / (c**2)
                F_net = (V_photon * rho - W_light) * g
                print_triad(flow, "NET KINETIC EJECTION (Newtons)", F_net)
            elif choice == '4':
                L = parser.evaluate(input(f"{Color.YELLOW}>> Input Inductance [H]: {Color.RESET}"))
                C = parser.evaluate(input(f"{Color.YELLOW}>> Input Capacitance [F]: {Color.RESET}"))
                print_triad(flow, "LC RESONANCE (Hz)", 1.0 / (2.0 * math.pi * math.sqrt(L * C)))
            elif choice == '5':
                f = parser.evaluate(input(f"{Color.YELLOW}>> Input Base Freq to Visualize [Hz]: {Color.RESET}"))
                plot_evanescent_wave(f)
        except Exception as e:
            print(f"{Color.RED}[!] Error: {e}{Color.RESET}")
        if choice != '5': input(f"{Color.CYAN}Press Enter to continue...{Color.RESET}")
