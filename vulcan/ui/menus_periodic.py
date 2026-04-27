import math
from vulcan.ui.header import clear_screen, print_header, Color
from vulcan.digital_root import get_dr_base10, get_dr_flow

def get_moon_geometry(z):
    if z <= 8: return "Cube (Vertices: 8)"
    elif z <= 14: return "Cube + Octahedron (Vertices: 14)"
    elif z <= 26: return "Nested Icosahedron (Vertices: 26)"
    elif z <= 46: return "Nested Dodecahedron (Vertices: 46)"
    elif z <= 92: return "Twin Nested Dodecahedra (Asymmetric Tension)"
    else: return "Transuranic Instability (Geometric Decay)"

def display_elements(flow):
    elements = [
        "Hydrogen (H)", "Helium (He)", "Lithium (Li)", "Beryllium (Be)", "Boron (B)", "Carbon (C)", "Nitrogen (N)", "Oxygen (O)", "Fluorine (F)", "Neon (Ne)",
        "Sodium (Na)", "Magnesium (Mg)", "Aluminum (Al)", "Silicon (Si)", "Phosphorus (P)", "Sulfur (S)", "Chlorine (Cl)", "Argon (Ar)", "Potassium (K)", "Calcium (Ca)",
        "Scandium (Sc)", "Titanium (Ti)", "Vanadium (V)", "Chromium (Cr)", "Manganese (Mn)", "Iron (Fe)", "Cobalt (Co)", "Nickel (Ni)", "Copper (Cu)", "Zinc (Zn)",
        "Gallium (Ga)", "Germanium (Ge)", "Arsenic (As)", "Selenium (Se)", "Bromine (Br)", "Krypton (Kr)", "Rubidium (Rb)", "Strontium (Sr)", "Yttrium (Y)", "Zirconium (Zr)",
        "Niobium (Nb)", "Molybdenum (Mo)", "Technetium (Tc)", "Ruthenium (Ru)", "Rhodium (Rh)", "Palladium (Pd)", "Silver (Ag)", "Cadmium (Cd)", "Indium (In)", "Tin (Sn)",
        "Antimony (Sb)", "Tellurium (Te)", "Iodine (I)", "Xenon (Xe)", "Cesium (Cs)", "Barium (Ba)", "Lanthanum (La)", "Cerium (Ce)", "Praseodymium (Pr)", "Neodymium (Nd)",
        "Promethium (Pm)", "Samarium (Sm)", "Europium (Eu)", "Gadolinium (Gd)", "Terbium (Tb)", "Dysprosium (Dy)", "Holmium (Ho)", "Erbium (Er)", "Thulium (Tm)", "Ytterbium (Yb)",
        "Lutetium (Lu)", "Hafnium (Hf)", "Tantalum (Ta)", "Tungsten (W)", "Rhenium (Re)", "Osmium (Os)", "Iridium (Ir)", "Platinum (Pt)", "Gold (Au)", "Mercury (Hg)",
        "Thallium (Tl)", "Lead (Pb)", "Bismuth (Bi)", "Polonium (Po)", "Astatine (At)", "Radon (Rn)", "Francium (Fr)", "Radium (Ra)", "Actinium (Ac)", "Thorium (Th)",
        "Protactinium (Pa)", "Uranium (U)", "Neptunium (Np)", "Plutonium (Pu)", "Americium (Am)", "Curium (Cm)", "Berkelium (Bk)", "Californium (Cf)", "Einsteinium (Es)", "Fermium (Fm)",
        "Mendelevium (Md)", "Nobelium (No)", "Lawrencium (Lr)", "Rutherfordium (Rf)", "Dubnium (Db)", "Seaborgium (Sg)", "Bohrium (Bh)", "Hassium (Hs)", "Meitnerium (Mt)", "Darmstadtium (Ds)",
        "Roentgenium (Rg)", "Copernicium (Cn)", "Nihonium (Nh)", "Flerovium (Fl)", "Moscovium (Mc)", "Livermorium (Lv)", "Tennessine (Ts)", "Oganesson (Og)"
    ]

    root_2 = math.sqrt(2.0)
    batch_size = 20

    for i in range(0, len(elements), batch_size):
        clear_screen()
        print_header()
        print(f"{Color.CYAN}--- ALCHEMICAL PERIODIC TABLE (ELEMENTS {i+1} TO {min(i+batch_size, len(elements))}) ---{Color.RESET}\n")
        print(f"{'Z':<4} | {'Element Name':<16} | {'Flow State':<12} | {'Evanescent':<16} | {'DR (B|F|E)':<12} | {'Moon Geometric State'}")
        print("-" * 115)

        for j in range(i, min(i + batch_size, len(elements))):
            z = j + 1
            flow_z = flow.convert(z)
            evan_z = flow.convert(z * root_2)

            dr_b = get_dr_base10(z)
            dr_f = get_dr_flow(flow_z)
            dr_e = get_dr_flow(evan_z)
            dr_str = f"{dr_b} | {dr_f} | {dr_e}"

            moon_geom = get_moon_geometry(z)
            print(f"{z:<4} | {elements[j]:<16} | {Color.GREEN}{flow_z:<12}{Color.RESET} | {Color.MAGENTA}{evan_z:<16}{Color.RESET} | {Color.YELLOW}{dr_str:<12}{Color.RESET} | {moon_geom}")

        action = input(f"\n{Color.YELLOW}Press Enter to continue (or type 'q' to quit list): {Color.RESET}")
        if action.lower() == 'q': break

def display_polyatomic_ions(flow):
    ions = [
        ("Ammonium", "NH4+", 11),
        ("Hydronium", "H3O+", 11),
        ("Hydroxide", "OH-", 9),
        ("Nitrate", "NO3-", 31),
        ("Nitrite", "NO2-", 23),
        ("Sulfate", "SO4_2-", 48),
        ("Sulfite", "SO3_2-", 40),
        ("Carbonate", "CO3_2-", 30),
        ("Phosphate", "PO4_3-", 47),
        ("Acetate", "CH3COO-", 32),
        ("Cyanide", "CN-", 13),
        ("Permanganate", "MnO4-", 57)
    ]
    root_2 = math.sqrt(2.0)
    clear_screen()
    print_header()
    print(f"{Color.CYAN}--- POLYATOMIC IONS (RESONANT ATOMIC SUMS) ---{Color.RESET}\n")
    print(f"{'Ion Name':<15} | {'Formula':<10} | {'Sum Z':<5} | {'Flow State':<12} | {'Evanescent':<16} | {'DR (B|F|E)':<12} | {'Moon Geometric Equivalent'}")
    print("-" * 125)
    for name, formula, z in ions:
        flow_z = flow.convert(z)
        evan_z = flow.convert(z * root_2)
        dr_b = get_dr_base10(z)
        dr_f = get_dr_flow(flow_z)
        dr_e = get_dr_flow(evan_z)
        dr_str = f"{dr_b} | {dr_f} | {dr_e}"
        moon_geom = get_moon_geometry(z)
        print(f"{name:<15} | {formula:<10} | {z:<5} | {Color.GREEN}{flow_z:<12}{Color.RESET} | {Color.MAGENTA}{evan_z:<16}{Color.RESET} | {Color.YELLOW}{dr_str:<12}{Color.RESET} | {moon_geom}")
    input(f"\n{Color.CYAN}Press Enter to return...{Color.RESET}")

def display_platonic_solids(flow):
    solids = [
        ("Tetrahedron", "Fire (Plasma)", "Alpha Particle / He", 4),
        ("Hexahedron (Cube)", "Earth (Solid)", "Oxygen (O)", 8),
        ("Octahedron", "Air (Gas)", "Silicon (Si)", 14),
        ("Icosahedron", "Water (Liquid)", "Iron (Fe)", 26),
        ("Dodecahedron", "Aether (Vacuum)", "Palladium (Pd)", 46)
    ]
    root_2 = math.sqrt(2.0)
    clear_screen()
    print_header()
    print(f"{Color.CYAN}--- THE CLASSICAL PLATONIC SOLIDS (ETHERIC GEOMETRIC ROOTS) ---{Color.RESET}")
    print("Mapping the Five Elements to Robert Moon's cumulative nuclear vertices.\n")
    print(f"{'Solid Name':<18} | {'Classical Element':<15} | {'Moon Completion':<18} | {'Z':<3} | {'Flow State':<12} | {'Evanescent':<16} | {'DR (B|F|E)'}")
    print("-" * 115)
    for name, elem, moon, z in solids:
        flow_z = flow.convert(z)
        evan_z = flow.convert(z * root_2)
        dr_b = get_dr_base10(z)
        dr_f = get_dr_flow(flow_z)
        dr_e = get_dr_flow(evan_z)
        dr_str = f"{dr_b} | {dr_f} | {dr_e}"
        print(f"{name:<18} | {elem:<15} | {moon:<18} | {z:<3} | {Color.GREEN}{flow_z:<12}{Color.RESET} | {Color.MAGENTA}{evan_z:<16}{Color.RESET} | {Color.YELLOW}{dr_str}{Color.RESET}")
    input(f"\n{Color.CYAN}Press Enter to return...{Color.RESET}")

def menu_periodic_table(flow):
    while True:
        clear_screen()
        print_header()
        print(f"{Color.CYAN}--- MODULE 4: ALCHEMICAL PERIODIC TABLE ---{Color.RESET}")
        print(f"{Color.GREEN} [1]{Color.RESET} View Elements 1-118 (Batched Display)")
        print(f"{Color.GREEN} [2]{Color.RESET} View Polyatomic Ions (Resonant Sums)")
        print(f"{Color.GREEN} [3]{Color.RESET} View Platonic Solids (Classical Elements & Moon Vertices)")
        print(f"{Color.RED} [0]{Color.RESET} Return to Main Menu\n")
        choice = input(f"{Color.YELLOW}>> Select Database: {Color.RESET}")
        if choice == '1': display_elements(flow)
        elif choice == '2': display_polyatomic_ions(flow)
        elif choice == '3': display_platonic_solids(flow)
        elif choice == '0': break
