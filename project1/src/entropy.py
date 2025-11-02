import numpy as np

def compute_entropy(freq):
    """Compute Shannon entropy (in bits) from frequency array."""
    p = freq / np.sum(freq)
    return -np.sum(p * np.log2(p))
