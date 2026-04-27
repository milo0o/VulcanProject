from vulcan.ui.header import clear_screen, print_header, Color

def menu_codex():
    while True:
        clear_screen()
        print_header()
        print(f"{Color.CYAN}--- MODULE 5: THE VULCAN CODEX (MASTER SCHEMATICS) ---{Color.RESET}")
        print(f"{Color.GREEN} [1]{Color.RESET} Volume I: The Vulcan Kinetics (Continuous Flow)")
        print(f"{Color.GREEN} [2]{Color.RESET} Volume II: Quantum Mechanics")
        print(f"{Color.GREEN} [3]{Color.RESET} Volume III: Electrical Engineering")
        print(f"{Color.GREEN} [4]{Color.RESET} Volume IV: Fundamental Constants Matrix")
        print(f"{Color.GREEN} [5]{Color.RESET} Volume V: Advanced Vector Kinetics & Topology")
        print(f"{Color.GREEN} [6]{Color.RESET} Volume VI: Working Hypotheses & Theories")
        print(f"{Color.GREEN} [7]{Color.RESET} Volume VII: The Vulcan Gate Engineering (Theoretical)")
        print(f"{Color.MAGENTA} [8]{Color.RESET} Volume VIII: Practical Prototypes (Real-World Infrastructure)")
        print(f"{Color.RED} [0]{Color.RESET} Return to Main Menu\n")

        choice = input(f"{Color.YELLOW}>> Select Codex Volume: {Color.RESET}")
        if choice == '0': break

        clear_screen()
        print_header()

        if choice == '1':
            print(f"{Color.MAGENTA}VOLUME I: THE VULCAN KINETICS{Color.RESET}\n")
            print(f"{Color.YELLOW}1. The Kinetic Weight of Light{Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} W = ((h * f) / c^2) * g")
            print("   Desc: Substitutes quantum energy into relativistic mass equivalence, yielding kinetic wave density.\n")
            print(f"{Color.YELLOW}2. Dynamic Gravitational Constant{Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} G_dynamic = (W_total * c^2) / (h * f)")
            print("   Desc: Solves for localized gravity by measuring kinetic drag on a photon.\n")
            print(f"{Color.YELLOW}3. Photon Probability Volume{Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} V = (pi * c^3) / (6 * f^3)")
            print("   Desc: The physical 4D cavity etched into spacetime by a propagating wave.\n")
            print(f"{Color.YELLOW}4. Reverse Lightning (Quantum Buoyancy){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} F_net = [ (V * rho_psi) - ((h * f) / c^2) ] * g")
            print("   Desc: Upward buoyant force when extreme electromagnetic tension compresses the vacuum.\n")

        elif choice == '2':
            print(f"{Color.MAGENTA}VOLUME II: QUANTUM MECHANICS{Color.RESET}\n")
            print(f"{Color.YELLOW}1. Planck-Einstein Relation{Color.RESET} (E = h * f)")
            print("   Desc: Energy is quantized and directly proportional to wave oscillation.\n")
            print(f"{Color.YELLOW}2. Mass-Energy Equivalence{Color.RESET} (m = E / c^2)")
            print("   Desc: The threshold where kinetic waves fold into solid geometry.\n")
            print(f"{Color.YELLOW}3. Heisenberg Uncertainty{Color.RESET} (Dx * Dp >= hbar / 2)")
            print("   Desc: Proves true rest (0 variance) is impossible; the ether constantly vibrates.\n")
            print(f"{Color.YELLOW}4. Schrödinger Equation{Color.RESET} (H_hat * psi = E * psi)")
            print("   Desc: Maps the probability cloud of the continuous wave prior to observation.\n")

        elif choice == '3':
            print(f"{Color.MAGENTA}VOLUME III: ELECTRICAL ENGINEERING{Color.RESET}\n")
            print(f"{Color.YELLOW}1. Ohm's Law{Color.RESET} (V = I * R)")
            print("   Desc: Etheric pressure (V) required to force kinetic flow (I) through structural friction (R).\n")
            print(f"{Color.YELLOW}2. Power Dissipation{Color.RESET} (P = I^2 * R)")
            print("   Desc: Thermodynamic entropy penalty of moving energy against geometric resistance.\n")
            print(f"{Color.YELLOW}3. LC Resonant Frequency{Color.RESET} (f_res = 1 / (2 * pi * sqrt(L * C)))")
            print("   Desc: The golden ratio where magnetic inertia and electric tension perfectly balance.\n")

        elif choice == '4':
            print(f"{Color.MAGENTA}VOLUME IV: FUNDAMENTAL CONSTANTS MATRIX{Color.RESET}\n")
            # Note: Since parser is not explicitly passed to menu_codex, you'd pull this from a global or instance if needed.
            # To maintain pure decoupling, you can pass parser as an argument to menu_codex, or hardcode the reference view.
            print(f"\n{Color.YELLOW}Note: Constants are natively loaded into the MathEvaluator.{Color.RESET}")

        elif choice == '5':
            print(f"{Color.MAGENTA}VOLUME V: ADVANCED VECTOR KINETICS & TOPOLOGY{Color.RESET}\n")
            print(f"{Color.YELLOW}1. Complex Vector Field Divergence (Riemann-Silberstein){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} Integral(Div(E + icB) dV) = Integral((E + icB) dS)")
            print(f"   {Color.CYAN}Variables:{Color.RESET} E = Electric Field (Real), icB = Magnetic Torsion (Imaginary)")
            print(f"   {Color.GREEN}Meaning:{Color.RESET} Evaluates a 3D spherical slice of a hypersphere. Separates the pushing expansion ")
            print("   of the electric field from the twisting torsion of the magnetic field. High imaginary values indicate ")
            print("   the spatial volume is attempting to drill a topological hole into the 4th dimension.\n")

            print(f"{Color.YELLOW}2. 3+1 Spacetime Decomposition (ADM Formalism){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} Integral(3D Spatial Volumes) dt = 4D Spacetime Block")
            print(f"   {Color.GREEN}Meaning:{Color.RESET} The geometric derivative of a 4D hypersphere is a 3D volume. By integrating ")
            print("   the physical displacement between sequential 3D volumes (frames), one algebraically isolates Time (t). ")
            print("   Time is defined not as a clock, but as the kinetic friction between cascading 3D geometries.\n")

            print(f"{Color.YELLOW}3. The Angle of Generation (Fine-Structure Constant){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} alpha = 1 / 137.035")
            print(f"   {Color.GREEN}Meaning:{Color.RESET} The mathematical boundary conditions of the Kaluza-Klein 5D compactification. ")
            print("   When the 5D normal vector projects into 3D, it compactifies at ~137 degrees. This structural angle ")
            print("   dictates the exact binding probability between pure light and physical baryonic matter.\n")

            print(f"{Color.YELLOW}4. The Trigonometric Firmament (Conservation of the Whole 1){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} sin^2(x) + cos^2(x) = 1  |  Intersect @ pi/4 = 1/sqrt(2)")
            print(f"   {Color.GREEN}Meaning:{Color.RESET} The absolute thermodynamic boundary of the macroscopic atom. ")
            print("   Kinetic waves and potential tension fold over 4 orthogonal rotations. The exact 45-degree ")
            print("   symmetry where these out-of-phase waves perfectly equalize yields the continuous 0.7071... ")
            print("   irrational vector, proving the universe mandates the root-2 exhaust to maintain the Whole 1.\n")

            print(f"{Color.YELLOW}5. Topologic Nucleus & The Hopf Fibration (Skyrmion Toroids){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} Bloch Sphere Vector -> Orthogonal 2D Larmor Precession")
            print(f"   {Color.GREEN}Meaning:{Color.RESET} The nucleus is not a rotating solid sphere, but a zero-friction ")
            print("   superfluid space. Kinetic spin is achieved via a quantized vortex (a hole) shifting its coordinates ")
            print("   at the pi/2 limit. The resulting geometric wake forms a Skyrmion Toroid, forcing the equatorial ")
            print("   plane to constantly, orthogonally warp to chase zero-sum equilibrium.\n")

        elif choice == '6':
            print(f"{Color.MAGENTA}VOLUME VI: WORKING HYPOTHESES & THEORIES{Color.RESET}\n")

            print(f"{Color.CYAN}I. The Quantum Archimedes Principle (Terrestrial Gamma-Ray Flashes){Color.RESET}")
            print("   A hydrodynamic model of quantum electrodynamics. A photon possesses an effective probability ")
            print("   volume bounded by its wavelength. In environments of extreme electromagnetic tension (e.g., ")
            print("   thunderstorm supercells), localized vacuum density (rho_psi) compresses. When the buoyant force ")
            print("   of the vacuum outpaces the kinetic weight of the photon, light is violently ejected upward against ")
            print("   gravity along the path of least etheric resistance.\n")

            print(f"{Color.CYAN}II. Hydrodynamic Wave Collapse & 4D Spacetime Cavities{Color.RESET}")
            print("   Extends Pilot-Wave theory via continuous kinetics. The propagating wave physically etches a 4D ")
            print("   probability cavity in the ether. Observation (a 'detector click') creates an instantaneous localized ")
            print("   pressure drop. The photon's kinetic mass fluidly rushes to fill this specific spatial cavity. ")
            print("   Wave-function collapse is thereby a scalar illusion, modeled by the Dirac Delta function, where ")
            print("   kinetic energy spikes to an absolute integer while un-chosen paths flatten into the continuous decimal ether.\n")

            print(f"{Color.CYAN}III. Geometric Refraction and the Inversion of Matter{Color.RESET}")
            print("   Asserts that stable physical matter ('Salt') manifests as a polarized geometric inversion of its ")
            print("   precursor kinetic architecture ('Mercury'). For example, the violently energetic tetrahedron of the ")
            print("   helium alpha-particle eclipses into total inert stability upon physical manifestation. Similarly, ")
            print("   the fluid, receptive geometry of the Icosahedron (Water) refracts through the polarity lens to ")
            print("   manifest physically as the rigid, penetrating geometry of Iron (Mars). Friction requires opposition.\n")

            print(f"{Color.CYAN}IV. 5D Kaluza-Klein Projection (The Golden Architecture){Color.RESET}")
            print("   Unifies electromagnetism and gravity through a 5-dimensional normal vector ('The Soul'). As this ")
            print("   higher-dimensional tether projects its shadow downward into 3D observable space, it compactifies. ")
            print("   The Fine-Structure Constant (1/137) is hypothesized not as a dimensionless scalar, but as the physical ")
            print("   intersection angle of this projection—acting as the universal regulator governing the materialization ")
            print("   of kinetic waves into physical geometry.\n")

            print(f"{Color.CYAN}V. Entropic Gravity & The Cosmic Hard Drive (Expansion via Complexity){Color.RESET}")
            print("   Expansion is not driven by an outward pushing 'Dark Energy', but by the Holographic Principle. ")
            print("   As the internal geometry (pion/gluon exchange) compounds in complexity, the universe must allocate ")
            print("   new 'null space' to record the quantum path back. Space is the physical manifestation of null ")
            print("   information. The universe physically expands its surface area (the Firmament) to prevent the ")
            print("   thermodynamic collapse of its own compounding data.\n")

            print(f"{Color.CYAN}VI. Majorana Consciousness & Degeneracy Pressure{Color.RESET}")
            print("   Consciousness is modeled as the ultimate Majorana Fermion (acting as its own antiparticle, perfectly ")
            print("   balancing the +1 and -1). To achieve internal coherence and identify the 'Self', it exerts Pauli ")
            print("   Exclusion forces. Physical volume (Space) is the topological exhaust of consciousness pushing the ")
            print("   external chaos of the 4D Bulk away to carve a stable, uncorrupted theater of observation.\n")

            print(f"{Color.CYAN}VII. The Hermetic Interaction Principle (Rest as the Pivot of Motion){Color.RESET}")
            print(f"   {Color.BOLD}Formula (conceptual):{Color.RESET} delta_p != 0  =>  exists frame where v_rel = 0")
            print("   Meaning: All physical interactions occur not in shared motion, but in contrary motion. ")
            print("   At the instant of collision or coupling, there exists a frame in which the interacting surfaces ")
            print("   are momentarily at rest relative to one another. This 'Hermetic still point' is the pivot ")
            print("   through which momentum, phase, and direction are exchanged.\n")

            print(f"{Color.CYAN}VIII. The Gear-Sine Phase Lattice (Discrete Vertices of a Continuous Wave){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} psi(n) = sin(w*n + phi)  |  s_n = sgn(psi(n)) in [+1, -1]")
            print("   Meaning: A line of coupled 'gears' (+1, -1, +1, -1) is modeled as discrete samples of a ")
            print("   continuous sine wave. The zero crossings are the Hermetic still points—where phase flips, ")
            print("   motion is exchanged, and a new direction is born. This lattice bridges continuous field and ")
            print("   discrete mechanism.\n")

            print(f"{Color.CYAN}IX. Generative Wave-Vertex Operator (Sine to i-Axis Projection){Color.RESET}")
            print(f"   {Color.BOLD}Formula:{Color.RESET} z(t) = x(t) + i*y(t) = e^(i(w*t + phi))")
            print("   Meaning: A real sine wave is lifted into the complex plane by a 90-degree phase shift, ")
            print("   tracing a circle. The i-axis component encodes the 'hidden' quadrature (etheric torsion), ")
            print("   while the real axis encodes observable motion. Vertices are defined at phase-flip events ")
            print("   (zero crossings). Geometry is not pre-given; it is generated by the continuous wave.\n")

        elif choice == '7':
            print(f"{Color.MAGENTA}VOLUME VII: THE VULCAN GATE ENGINEERING (THEORETICAL){Color.RESET}\n")

            print(f"{Color.CYAN}I. The Macroscopic Meissner Funnel{Color.RESET}")
            print("   Utilizing an excessively symmetrical Toroid (via BEC, cryogenics, or acoustic quartz resonance). ")
            print("   By achieving a frictionless macroscopic quantum state, the Toroid acts as a perfect diamagnet, ")
            print("   violently expelling all ambient magnetic chaos. The toroidal geometry forces this expelled ")
            print("   vacuum pressure into the center hole, crushing chaotic ambient energy into a hyper-dense, ")
            print("   unidirectional 1D magnetic jet without requiring an internal power source.\n")

            print(f"{Color.CYAN}II. Chiral Fusion & The Spawn Timer (Feshbach Resonance){Color.RESET}")
            print("   Bypassing the Coulomb barrier via the 4D Bulk. A localized Bose-Einstein Condensate acts as a ")
            print("   magnetic 'Monitor Mode', expanding the De Broglie wavelengths until collision meshes dissolve. ")
            print("   Atoms are slid into the exact same (0,0,0,0) coordinate as pure potential. When the external ")
            print("   magnetic trap is 'snapped' off, the universe's engine ticks, forcing instantaneous Decoherence. ")
            print("   The overlapping geometries flawlessly lock, violently exhaling the kinetic difference as ")
            print("   evanescent radiation.\n")

            print(f"{Color.CYAN}III. The Cosmic Newton's Cradle (Rebound Harvesting){Color.RESET}")
            print("   The atom operates as a 3-field system: The Proton (Mover), the Electron (Counterweight), and ")
            print("   the asymmetrical Neutron excess (The Null Space Buffer). Energy transfers as an invisible ")
            print("   pion wave. The Vulcan Gate's mechanical switch must be timed to the exact Larmor frequency to ")
            print("   intercept the rebounding wave traversing the neutral medium, siphoning the translated kinetic ")
            print("   data before it strikes the Proton core.\n")

        elif choice == '8':
            print(f"{Color.MAGENTA}VOLUME VIII: PRACTICAL PROTOTYPES (REAL-WORLD INFRASTRUCTURE){Color.RESET}\n")
            print("These prototypes represent the physical infrastructure layer of the Vulcan Project.\n")

            print(f"{Color.CYAN}Prototype A — The Hemp Structural Engine{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} High-yield, carbon-negative biomaterial replacing plastics, concrete, textiles.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Hempcrete walls, fiber composites, hurd insulation, biomass pyrolysis.")

            print(f"\n{Color.CYAN}Prototype B — The Algae Bio-Industrial Reactor{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Vertical bioreactor for oils, proteins, polymers. Grows 10-20x faster.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Vertical tubes, nutrient cycling, bioplastics, biofuels, fertilizer.")

            print(f"\n{Color.CYAN}Prototype C — The Stirling Gradient Engine{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Extracts energy from any temp difference (ground/air, day/night).")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Off-grid mechanical power, low-maintenance electricity in any climate.")

            print(f"\n{Color.CYAN}Prototype D — The Tidal / Current Turbine Node{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Hydrokinetic harvesting from rivers, tides, and ocean currents.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Slow-RPM/high-torque turbines, fish-safe blades, submerged microgrids.")

            print(f"\n{Color.CYAN}Prototype E — The Geothermal Loop Engine{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Taps stable Earth subsurface temps (~55°F) for heating/cooling.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Ground loops, heat pumps, Stirling-geothermal hybrid systems.")

            print(f"\n{Color.CYAN}Prototype F — The Piezoelectric Kinetic Floor{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Pressure on piezoelectric tiles generates electricity from motion.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Walkways, chicken paths, gateways, barn floors.")

            print(f"\n{Color.CYAN}Prototype G — The Graphene Moth-Eye EM Harvester{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Patterned graphene absorbs ambient EM radiation across a broad spectrum.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} EM scrubber panels, RF harvesting, waste-signal reclamation.")

            print(f"\n{Color.CYAN}Prototype H — The Salinity Gradient Engine{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Osmotic power from freshwater and saltwater separated by a membrane.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Pressure-retarded osmosis (PRO), reverse electrodialysis (RED).")

            print(f"\n{Color.CYAN}Prototype I — The Waste-to-Energy Pyrolysis Forge{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Thermal decomposition of organic waste without oxygen.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Syngas, bio-oil, and biochar production via retort kilns/gasifiers.")

            print(f"\n{Color.CYAN}Prototype J — The Vertical Hydroponic Tower{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} High-density food production yielding massive output on minimal land.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} NFT channels, drip towers, LED-assisted growth, closed nutrient loops.")

            print(f"\n{Color.CYAN}Prototype K — The Rainwater Capture & Filtration Node{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Water independence system: rainwater -> storage -> filtration -> potable.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} First-flush diverters, sand/charcoal filters, UV sterilization.")

            print(f"\n{Color.CYAN}Prototype L — The Microgrid Control Hub{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Distributed energy management. Redundancy = resilience.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Integrates Solar, Stirling, Tidal, Geothermal, Piezo, and EM nodes.")

            print(f"\n{Color.CYAN}Prototype M — The Soil Remediation Engine{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Healing contaminated land via plants, fungi, and microbes.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Hemp (heavy metals), Fungi (hydrocarbons), Sunflowers (lead), Biochar.")

            print(f"\n{Color.CYAN}Prototype N — The Closed-Loop Nutrient Cycle{Color.RESET}")
            print(f"   {Color.BOLD}Core Idea:{Color.RESET} Zero-waste agriculture: waste -> compost -> soil -> plants -> food.")
            print(f"   {Color.GREEN}Functions:{Color.RESET} Composting, vermiculture, biochar soil amendment.")

        input(f"\n{Color.CYAN}Press Enter to return to Codex Index...{Color.RESET}")
