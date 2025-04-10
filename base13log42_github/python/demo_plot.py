import numpy as np
import matplotlib.pyplot as plt
from resonance_engine import calculate_resonance

def plot_symbolic_cycle():
    """
    Plot the symbolic cycle and resonance transitions over time.
    """
    states = np.arange(1, 13)  # Symbolic states from 1 to 12
    depths = np.arange(1, 6)   # Recursion depths from 1 to 5
    
    # Set up the figure
    plt.figure(figsize=(10, 6))
    
    for n in depths:
        resonance_values = [calculate_resonance(state, n) for state in states]
        plt.plot(states, resonance_values, label=f"Depth {n}")
    
    plt.title("Symbolic State Resonance at Different Recursion Depths")
    plt.xlabel("Symbolic State")
    plt.ylabel("Resonance")
    plt.xticks(states)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_symbolic_cycle()
