import wordcount as wc
import operator
results, freq = wc.wordcount('data\project1\gettysburg.txt')
sorted_words = list(reversed(sorted(results.items(), key=lambda kv: kv[1])))
print(sorted_words)
