try:
    import numpy as np
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

from vulcan.ui.header import Color

def plot_evanescent_wave(f_val):
    if not MATPLOTLIB_AVAILABLE:
        print(f"{Color.RED}[!] Matplotlib not installed. Cannot initialize visualizer.{Color.RESET}")
        return
    visual_f = f_val
    while visual_f > 1000: visual_f /= 10.0
    x = np.linspace(0, 4 * np.pi, 1000)
    y_base = np.sin(x * visual_f)
    y_evan = np.sin(x * visual_f * np.sqrt(2.0))
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 5))
    plt.plot(x, y_base, color='cyan', label=f'Static Base Wave', alpha=0.7)
    plt.plot(x, y_evan, color='magenta', label=f'Evanescent Wave (x √2)', alpha=0.9, linestyle='--')
    plt.title("Visualizer: The Evanescent Phase Shift (Tension of Space)", color='white')
    plt.xlabel("Continuous Flow Time", color='white')
    plt.ylabel("Kinetic Amplitude", color='white')
    plt.legend()
    plt.grid(color='gray', linestyle=':', alpha=0.4)
    print(f"{Color.GREEN}[+] Launching Matplotlib Visualizer HUD...{Color.RESET}")
    plt.show()
