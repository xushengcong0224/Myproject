import matplotlib.pyplot as plt
import numpy as np
import os


def _save_path(*parts):
    """Return a valid path in the plots/ directory."""
    pdir = os.path.join(os.path.dirname(__file__), "..", "plots")
    os.makedirs(pdir, exist_ok=True)
    return os.path.join(pdir, *parts)


def plot_rank_frequency(counts):
    """Plot Zipf-style rank-frequency relationship (log–log)."""
    ranks = np.arange(1, len(counts) + 1)
    freq_sorted = np.sort(counts)[::-1]

    plt.figure(figsize=(8, 6))
    plt.loglog(ranks, freq_sorted, ".", label="word pairs")
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Word-Pair Rank–Frequency (log–log)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    path = _save_path("freq_distribution.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"✅ Saved: {path}")


def plot_cumulative(counts):
    """Plot the cumulative distribution of word-pair frequencies."""
    freq_sorted = np.sort(counts)[::-1]
    cum = np.cumsum(freq_sorted) / freq_sorted.sum()
    x = np.arange(1, len(freq_sorted) + 1)

    plt.figure(figsize=(8, 6))
    plt.plot(x, cum)
    plt.xlabel("Top-k word pairs")
    plt.ylabel("Cumulative share")
    plt.title("Cumulative Distribution of Word-Pair Frequencies")
    plt.grid(True, linestyle="--", linewidth=0.5)
    path = _save_path("cumulative_distribution.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"✅ Saved: {path}")
