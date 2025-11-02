import os
import re
import numpy as np

def wordcount(filename):
    """Read a text file, split into words, and return a word-count dictionary and normalized frequency array."""
    base_path = os.path.dirname(__file__)
    filepath = os.path.join(base_path, '..', 'data', filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        s = f.read()

    words = re.split(r"[\W\s\!+\.+,+\?+\"]", s)
    empties = words.count('')

    dicto = {}
    for w in words:
        if w:
            dicto[w] = dicto.get(w, 0) + 1

    freq = np.array(sorted(dicto.values())[::-1]) / float(len(words) - empties) * 100
    return dicto, freq
