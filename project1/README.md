# Project 1 — Word Frequency & Entropy (Zipf’s Law Exploration)

## Overview
This project investigates statistical regularities of natural language through quantitative text analysis. It examines the relationship between word frequency distributions and Shannon entropy, demonstrating the emergence of Zipf’s Law in real-world language data.

We analyze two historically significant English texts:
1. Abraham Lincoln’s _Gettysburg Address_ (1863)  
2. John F. Kennedy’s _Inaugural Address_ (1961)

Through word frequency distributions, log–log scaling, and entropy calculations, we explore how linguistic diversity and redundancy reflect principles of information theory.

---

## Objectives
1. Empirically verify Zipf’s Law — test whether word frequencies follow an approximate power-law relationship where frequency decreases roughly in proportion to rank.  
2. Quantify linguistic information content — use Shannon entropy to measure vocabulary diversity and unpredictability.  
3. Compare speeches across eras — investigate whether stylistic or linguistic complexity differs between the two speeches.

---

## Background (Plain Language)
- **Zipf’s Law**: When you sort words by how often they appear, the 1st most common word appears about twice as often as the 2nd, three times as often as the 3rd, and so on. On a log–log plot of frequency versus rank, this looks like a straight, downward‑sloping line.
- **Shannon Entropy**: Entropy summarizes how “spread out” the word usage is. If a text repeatedly uses the same few words, entropy is lower; if a text uses a wider variety of words with more even frequencies, entropy is higher.

---

## Project Structure
```
project1/
├── data/
│   ├── gettysburg.txt
│   └── inaugural_address_jfk.txt
├── plots/
│   └── zipf_comparison.png
├── src/
│   ├── wordcount.py
│   ├── entropy.py
│   ├── visualize.py
│   └── main.py
└── requirements.txt
```

**Modules**
- `wordcount.py`: Reads text, removes punctuation, and counts word occurrences.
- `entropy.py`: Computes Shannon entropy from the normalized word-frequency array.
- `visualize.py`: Plots word-frequency distributions on a log–log scale and saves the figure.
- `main.py`: Orchestrates the pipeline: load data → compute frequencies → compute entropy → plot and report results.

---

## Installation
Run the following from inside the `project1` directory:
```bash
cd project1
pip install -r requirements.txt
```

Dependencies:
- `numpy` — numerical computation
- `matplotlib` — plotting

---

## Running the Analysis
Run the main pipeline:
```bash
python src/main.py
```

Expected console output (illustrative):
```
==============================
  Shannon Entropy Comparison
==============================
Gettysburg Address: 6.42 bits
JFK Inaugural Address: 7.83 bits
✅ Plot saved to plots/zipf_comparison.png
```

A figure named `zipf_comparison.png` will be saved in the `plots/` folder.

---

## Results and Interpretation (Example)
| Speech | Word Count | Distinct Words | Entropy (bits) | Observation |
|--------|------------|----------------|----------------|-------------|
| Gettysburg Address | ~270 | ~140 | 6.4 | Concise and repetitive — lower entropy |
| JFK Inaugural Address | ~1,300 | ~600 | 7.8 | Broader vocabulary — higher entropy |

**Discussion**
- Both distributions typically appear near‑linear on a log–log plot, consistent with Zipf‑like behavior.  
- JFK’s address tends to show higher entropy, indicating richer vocabulary and greater unpredictability of word choice.

---

## Extensions
- Add stopword filtering and lemmatization for refined counts.  
- Compare across genres (political speeches, news, literature).  
- Estimate the power‑law slope via regression and report goodness‑of‑fit.  
- Explore other languages or multi‑text averages.  
- Visualize rank–frequency using cumulative distributions or log bins.

---

## References
- Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort.*  
- Shannon, C. E. (1948). *A Mathematical Theory of Communication.* Bell System Technical Journal.  
- Piantadosi, S. T. (2014). “Zipf’s word frequency law in natural language: A critical review and future directions.” *Psychonomic Bulletin & Review.*

---

## Author
Shengcong Xu 
Brandeis University 
License: MIT
