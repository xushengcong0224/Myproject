from src.entropy_calc import shannon_entropy_from_counts
from src.parse_data import load_word_pairs_data, top_n_pairs
from src.visualize import plot_rank_frequency, plot_cumulative
from src.word_pairs import (
    build_top_k_graph,
    draw_word_pair_graph,
    longest_simple_path,
    connectivity_report,
)


def main():
    # Load dataset
    words, idx1, idx2, freq = load_word_pairs_data()

    # === Q1: Inspect the 100 most common word pairs ===
    top100 = top_n_pairs(words, idx1, idx2, freq, n=100)
    print("\nTop 100 Most Common English Word Pairs")
    print("--------------------------------------")
    for i, (w1, w2, c) in enumerate(top100, start=1):
        print(f"{i:>2}. {w1:>12s} -> {w2:<12s} (freq = {c})")

    # Compute Shannon entropy of the word-pair distribution
    H = shannon_entropy_from_counts(freq)
    print(f"\nShannon Entropy (word-pair distribution): {H:.3f} bits")

    # Plot Zipf-style and cumulative distributions
    plot_rank_frequency(freq)
    plot_cumulative(freq)

    # === Q2: Directed graph of top-20 word pairs ===
    G = build_top_k_graph(words, idx1, idx2, freq, k=20)
    draw_word_pair_graph(G, filename="word_pairs.png")
    seq = longest_simple_path(G)
    print("\nLongest word sequence within top-20 graph:")
    print(" -> ".join(seq))

    # === Q3: Graph connectivity analysis ===
    is_sc, n_weak, weak_comps = connectivity_report(G)
    print("\nGraph Connectivity (top-20 word pairs)")
    print("--------------------------------------")
    print(f"Strongly connected: {is_sc}")
    print(f"Weakly connected components: {n_weak}")
    if n_weak > 1:
        for i, comp in enumerate(weak_comps, 1):
            print(f"  Component {i}: {', '.join(comp)}")


if __name__ == "__main__":
    main()
