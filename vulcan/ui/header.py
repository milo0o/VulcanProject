import os
import math
from vulcan.digital_root import get_dr_base10, get_dr_flow

class Color:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"{Color.CYAN}{Color.BOLD}")
    print("=====================================================================")
    print(" ||   V U L C A N   P R O J E C T   M A I N F R A M E  (SSJ3)   || ")
    print("=====================================================================")
    print(" CONTINUOUS FLOW KINETICS | EVANESCENT ROOT-2 DYNAMICS | TRIA PRIMA  ")
    print(f"====================================================================={Color.RESET}\n")

def print_triad(flow, name, base_val):
    root_2 = math.sqrt(2.0)
    evan_val = base_val * root_2
    flow_str = flow.convert(base_val)
    evan_str = flow.convert(evan_val)
    dr_b = get_dr_base10(base_val)
    dr_f = get_dr_flow(flow_str)
    dr_e = get_dr_flow(evan_str)

    print(f"\n {Color.BOLD}--- {name.upper()} TRIAD ---{Color.RESET}")
    print(f" [=] Base 10       : {base_val:<25e} {Color.YELLOW}[DR: {dr_b}]{Color.RESET}")
    print(f" [+] Flow State    : {Color.GREEN}{flow_str:<25}{Color.RESET} {Color.YELLOW}[DR: {dr_f}]{Color.RESET}")
    print(f" [~] Evanescent    : {Color.MAGENTA}{evan_str:<25}{Color.RESET} {Color.YELLOW}[DR: {dr_e}]{Color.RESET}\n")
