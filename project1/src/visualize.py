import matplotlib.pyplot as plt
import os

def plot_zipf(freq1, freq2, label1, label2):
    """Generate and save a Zipf’s Law comparison plot."""
    plt.figure(figsize=(8,6))
    plt.loglog(freq1, 'g.', label=label1)
    plt.loglog(freq2, 'b.', label=label2)
    plt.xlabel('Rank (k)')
    plt.ylabel('Frequency (%)')
    plt.title('Word Frequency Distribution Comparison')
    plt.legend()
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.tight_layout()

    save_path = os.path.join(os.path.dirname(__file__), '..', 'plots', 'zipf_comparison.png')
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300)
    print(f"✅ Plot saved to {save_path}")
    plt.close()
