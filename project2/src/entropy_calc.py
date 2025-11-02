import numpy as np


def shannon_entropy_from_counts(counts):
    """
    Compute Shannon entropy in bits from a vector of counts.
    """
    counts = counts.astype(float)
    total = counts.sum()
    if total <= 0:
        return 0.0
    p = counts / total
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))
