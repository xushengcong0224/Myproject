# Project 2 — English Language Word Pairs (Shannon Analysis)

## 📘 Overview
This project reproduces Shannon’s analysis of **word-pair frequency distributions** in English.  
It uses data from the **Corpus of Contemporary American English (COCA)** to examine over one million word pairs, computes their information content, and visualizes the structure of the most frequent combinations.

---

## 🎯 Objectives
1. **Inspect the 100 most common word pairs** in English.  
2. **Visualize the 20 most common word pairs** as a directed graph and find the longest sequence that can be formed.  
3. **Analyze graph connectivity** — determine whether it is strongly connected and list its weakly connected components.  
4. **Quantify information content** using Shannon entropy and Zipf-like frequency plots.

---

## 🧩 Project Structure
```
project2/
├── data/
│   ├── words.txt
│   ├── word1_index.txt
│   ├── word2_index.txt
│   └── frequencies.txt
├── plots/
│   ├── freq_distribution.png
│   ├── cumulative_distribution.png
│   └── word_pairs.png
├── src/
│   ├── parse_data.py
│   ├── entropy_calc.py
│   ├── visualize.py
│   ├── word_pairs.py
│   └── main.py
└── requirements.txt
```

---

## ⚙️ Installation
```bash
cd project2
pip install -r requirements.txt
```
**Dependencies:** `numpy`, `matplotlib`, `networkx`

---

## 🚀 Running the Analysis
```bash
python src/main.py
```

### Expected Console Output
```
Top 100 Most Common English Word Pairs
--------------------------------------
 1. of -> the      (freq = 657504)
 2. in -> the      (freq = 614276)
 ...

Shannon Entropy (word-pair distribution): 10.83 bits
✅ Saved: plots/freq_distribution.png
✅ Saved: plots/cumulative_distribution.png
✅ Saved: plots/word_pairs.png

Longest word sequence within top-20 graph:
of -> the -> people -> of -> the -> country

Graph Connectivity (top-20 word pairs)
--------------------------------------
Strongly connected: False
Weakly connected components: 3
Component 1: [a, and, be, in, on, the, to, of]
...
```

---

## 📊 Visualizations
- **Rank–Frequency Distribution** (`plots/freq_distribution.png`)  
  Shows the Zipf-like relationship between rank and frequency.  
- **Cumulative Distribution** (`plots/cumulative_distribution.png`)  
  Demonstrates how quickly common word pairs dominate the corpus.  
- **Directed Graph of Top 20 Word Pairs** (`plots/word_pairs.png`)  
  Nodes represent words; arrows indicate the most common transitions (`word1 → word2`).  

---

## 📈 Analytical Tasks and Results

### 1️⃣ Inspect the 100 Most Common Pairs
The list confirms that function words dominate English pair frequencies (e.g., “of the”, “in the”, “to be”, “for the”).  
Such patterns reflect syntactic rules rather than semantic content.

### 2️⃣ Visualize the Top 20 Pairs and Find the Longest Sequence
A directed graph is built from the 20 most frequent pairs.  
The longest path represents a chain of words that can appear successively under the observed frequencies.  
For example: `of → the → people → of → the → country`.

### 3️⃣ Graph Connectivity
Using NetworkX analysis:
- The graph is **not strongly connected**.  
- It consists of multiple weakly connected components, each corresponding to localized word clusters.  

---

## 🧠 Information Theory Insight
The Shannon entropy of ≈ 10.8 bits/word pair quantifies the average information content.  
The Zipf-like curve reveals the expected power-law distribution, illustrating that a small subset of word pairs carries a large fraction of usage.

---

## 🧾 References
- Shannon, C. E. (1948). *A Mathematical Theory of Communication.* Bell System Technical Journal.  
- Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort.*  
- Cover & Thomas (2006). *Elements of Information Theory.*

---

## 👨‍💻 Author
**Shengcong Xu**  
Brandeis University  
License: MIT
