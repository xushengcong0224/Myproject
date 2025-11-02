import os
import matplotlib.pyplot as plt
import networkx as nx


def _plots_dir():
    """Ensure plots/ directory exists and return its path."""
    p = os.path.join(os.path.dirname(__file__), "..", "plots")
    os.makedirs(p, exist_ok=True)
    return p


def build_top_k_graph(words, index1, index2, freq, k=20):
    """Construct a directed graph from the top-k most frequent word pairs."""
    G = nx.DiGraph()
    k = min(k, len(freq))
    for i in range(k):
        w1 = words[int(index1[i])]
        w2 = words[int(index2[i])]
        w = int(freq[i])
        G.add_edge(w1, w2, weight=w)
    return G


def draw_word_pair_graph(G, filename="word_pairs.png"):
    """Draw the directed graph in circular layout and label edges."""
    pos = nx.circular_layout(G)
    plt.figure(figsize=(9, 9))
    nx.draw_networkx_nodes(G, pos, node_color="#9ed0ff", node_size=2500, edgecolors="#336699")
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=18, width=1.5, edge_color="#444")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("20 Most Common English Word Pairs (Directed Graph)")
    plt.axis("off")
    out = os.path.join(_plots_dir(), filename)
    plt.tight_layout()
    plt.savefig(out, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"✅ Saved: {out}")


def longest_simple_path(G):
    """
    Find the longest simple path (no repeated nodes) using DFS.
    Works efficiently for small graphs (k ≤ 20).
    """
    best = []

    def dfs(node, visited, path):
        nonlocal best
        visited.add(node)
        path.append(node)
        if len(path) > len(best):
            best = path.copy()
        for nbr in G.successors(node):
            if nbr not in visited:
                dfs(nbr, visited, path)
        path.pop()
        visited.remove(node)

    for start in G.nodes:
        dfs(start, set(), [])
    return best


def connectivity_report(G):
    """
    Evaluate whether the directed graph is strongly connected.
    Also list weakly connected components.
    """
    is_sc = nx.is_strongly_connected(G)
    weak_components = list(nx.weakly_connected_components(G))
    return is_sc, len(weak_components), [sorted(list(c)) for c in weak_components]
