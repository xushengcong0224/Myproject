# Natural Language Information Analysis

This repository contains two independent mini-projects exploring English text statistics through Shannon’s information-theoretic perspective.

---

## 📁 Project Structure
```
Myproject/
├── project1/
│   ├── data/           # Gettysburg & JFK texts
│   ├── plots/          # Zipf comparison, entropy charts
│   ├── src/            # Python scripts for Project 1
│   ├── README.md       # Detailed explanation for Project 1
│   └── requirements.txt
│
├── project2/
│   ├── data/           # COCA word-pair dataset
│   ├── plots/          # Frequency and graph visualizations
│   ├── src/            # Python scripts for Project 2
│   ├── README.md       # Detailed explanation for Project 2
│   └── requirements.txt
│
├── README.md           # (this file)
└── requirements.txt    # shared dependencies
```

---

## 🧪 Project 1 — Word Frequency and Shannon Entropy
Analyzes the **Gettysburg Address** and **JFK Inaugural Address**.  
It counts word frequencies, compares their Zipf-like distributions, and computes Shannon entropy to measure information content.

**Key features**
- Tokenize text and compute normalized frequency distributions  
- Plot rank-frequency curves on log–log scales  
- Compare entropies between documents  

**Run**
```bash
cd project1
python -m src.main
```

---

## 🧠 Project 2 — English Word Pairs (Shannon Bigram Analysis)
Implements Shannon’s bigram frequency model using COCA corpus data.  
It visualizes the 20 most frequent word pairs as a directed graph and examines connectivity.

**Key features**
- Parse `words.txt`, `word1_index.txt`, `word2_index.txt`, and `frequencies.txt`  
- Compute word-pair entropy and Zipf-like distributions  
- Draw directed graphs of top-20 pairs  
- Identify longest simple sequences and graph connectivity  

**Run**
```bash
cd project2
python -m src.main
```

---

## ⚙️ Requirements
To install all dependencies for both projects:
```bash
pip install -r requirements.txt
```

---

## 🧩 Technologies
| Library | Purpose |
|----------|----------|
| **NumPy** | Numeric computation, frequency arrays |
| **Matplotlib** | Data visualization |
| **NetworkX** | Directed-graph analysis |
| **Python 3.10+** | Core language |

---

## 🧾 References
- Claude E. Shannon (1948) *“A Mathematical Theory of Communication.”*  
- George K. Zipf (1949) *“Human Behavior and the Principle of Least Effort.”*  
- Cover & Thomas (2006) *“Elements of Information Theory.”*

---

## 👨‍💻 Author
**Shencong Xu**  
Brandeis University  
License: MIT
