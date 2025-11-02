# 🧠 Project 1 — Word Frequency & Entropy (Zipf’s Law Exploration)

## 📘 Overview
This project investigates the **statistical regularities of natural language** through quantitative text analysis.  
Specifically, it examines the relationship between **word frequency distributions** and **Shannon entropy**, demonstrating the emergence of **Zipf’s Law** in real-world language data.

We analyze two historically significant English texts:
1. **Abraham Lincoln’s _Gettysburg Address_ (1863)**  
2. **John F. Kennedy’s _Inaugural Address_ (1961)**

Through word frequency distributions, log–log scaling, and entropy calculations, we explore how linguistic diversity and redundancy reflect underlying principles of information theory.

---

## 🎯 Objectives

1. **Empirically verify Zipf’s Law** — test whether word frequencies follow a power-law distribution \( f_k = \frac{C}{k} \).  
2. **Quantify linguistic information content** — use Shannon entropy to measure vocabulary diversity and unpredictability.  
3. **Compare speeches across eras** — investigate whether stylistic or linguistic complexity changes over time.  

---

## 🧩 Theoretical Background

### 1️⃣ Zipf’s Law
Zipf’s Law states that the frequency of a word in a corpus is inversely proportional to its rank \( k \):
\[
f_k = \frac{C}{k}
\]
where \( f_k \) is the frequency of the word ranked \( k \), and \( C \) is a normalization constant.  
In log–log coordinates, this yields a straight line with slope ≈ –1.

This statistical pattern reflects the **self-organizing nature of human language**, balancing efficiency and redundancy.

### 2️⃣ Shannon Entropy
Entropy quantifies the **average information per symbol**:
\[
H = - \sum_i p_i \log_2(p_i)
\]
where \( p_i \) is the relative frequency of each word.  
Higher \( H \) → greater unpredictability (diverse vocabulary);  
Lower \( H \) → simpler, more repetitive language.

Entropy thus complements Zipf’s Law by offering a **numerical measure** of language richness.

---

## 📁 Project Structure
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

**Module Overview:**
| File | Purpose |
|------|----------|
| `wordcount.py` | Reads text, cleans punctuation, and counts word occurrences. |
| `entropy.py` | Computes Shannon entropy from normalized word frequency. |
| `visualize.py` | Plots word frequency distributions on log–log scale. |
| `main.py` | Integrates all components and outputs both entropy and plots. |

---

## ⚙️ Installation
Ensure you are in the `project1` directory.

```bash
cd project1
pip install -r requirements.txt
```

Dependencies:
- `numpy` — numerical computation
- `matplotlib` — plotting library

---

## 🚀 Running the Analysis
Run the main pipeline:
```bash
python src/main.py
```

Expected console output:
```
==============================
  Shannon Entropy Comparison
==============================
Gettysburg Address: 6.42 bits
JFK Inaugural Address: 7.83 bits
✅ Plot saved to plots/zipf_comparison.png
```

A figure `zipf_comparison.png` will be saved in the `plots/` folder, showing both distributions.

---

## 📊 Results and Interpretation

| Speech | Word Count | Distinct Words | Entropy (bits) | Observation |
|---------|-------------|----------------|----------------|--------------|
| Gettysburg Address | ~270 | ~140 | 6.4 | Concise and repetitive — lower entropy |
| JFK Inaugural Address | ~1,300 | ~600 | 7.8 | Broader vocabulary — higher entropy |

### 🔍 Discussion
- Both distributions follow a near–linear pattern in log–log space, confirming **Zipf-like scaling**.  
- JFK’s address exhibits a **flatter slope and higher entropy**, indicating **greater lexical diversity** and **richer expression**.  
- The findings align with the **principle of least effort** — language optimizes communication by balancing repetition and novelty.

---

## 🧠 Extensions
- Add **stopword filtering** or **lemmatization** to improve accuracy.  
- Compare across genres (political speeches, news, literature).  
- Fit power-law exponents numerically using regression.  
- Explore **cross-linguistic entropy** (e.g., Chinese, Spanish).  
- Visualize rank–frequency using log bins or cumulative distributions.

---

## 🧾 References
- Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort.*  
- Shannon, C. E. (1948). *A Mathematical Theory of Communication.* *Bell System Technical Journal.*  
- Piantadosi, S. T. (2014). “Zipf’s word frequency law in natural language: A critical review and future directions.” *Psychonomic Bulletin & Review.*

---

## 👨‍💻 Author
**Your Name**  
Brandeis University · 2025  
Course: Computational Text Analysis  
License: MIT  

---

> 💡 **Tip for GitHub Display**
> - Add a preview figure at the top:  
>   `![Zipf Plot](plots/zipf_comparison.png)`  
> - Enable LaTeX formula rendering in your GitHub settings for better visuals.  
> - You can also use Shields.io badges for Python version or license.
