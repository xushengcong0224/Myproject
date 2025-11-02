import os
import numpy as np


def _here(*parts):
    """Return an absolute path inside this project."""
    return os.path.join(os.path.dirname(__file__), *parts)


def load_word_pairs_data():
    """
    Load the four text files:
      - words.txt              (ISO-8859-1 encoding)
      - word1_index.txt, word2_index.txt (UTF-8, whitespace-separated integers)
      - frequencies.txt        (counts, already sorted in descending order)

    Returns
    -------
    words : list[str]
    index1, index2 : np.ndarray[int]
    freq : np.ndarray[int]
    """
    data_dir = _here("..", "data")

    # words.txt (teacher’s hint: ISO-8859-1 encoding)
    with open(os.path.join(data_dir, "words.txt"), "r", encoding="ISO-8859-1") as f:
        words = [w for w in f.read().split() if w]

    # helper to read integer lists
    def read_ints(path):
        with open(path, "r", encoding="utf-8") as f:
            tokens = f.read().split()
        return np.array([int(t) for t in tokens], dtype=int)

    index1 = read_ints(os.path.join(data_dir, "word1_index.txt"))
    index2 = read_ints(os.path.join(data_dir, "word2_index.txt"))

    with open(os.path.join(data_dir, "frequencies.txt"), "r", encoding="utf-8") as f:
        freq = np.array([int(float(t)) for t in f.read().split()], dtype=int)

    n = min(len(index1), len(index2), len(freq))
    if n == 0:
        raise ValueError("No data loaded; please check input files.")
    if len(index1) != len(index2) or len(index1) != len(freq):
        index1, index2, freq = index1[:n], index2[:n], freq[:n]

    return words, index1, index2, freq


def top_n_pairs(words, index1, index2, freq, n=100):
    """Return the top-n word pairs (word1, word2, count)."""
    n = min(n, len(freq))
    return [
        (words[int(index1[i])], words[int(index2[i])], int(freq[i]))
        for i in range(n)
    ]
