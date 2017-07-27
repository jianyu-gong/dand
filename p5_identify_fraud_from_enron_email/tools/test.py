words = "running sister logical logic"
from nltk.stem.snowball import SnowballStemmer

words = words.split()
print words
stemmer = SnowballStemmer("english")

word_split =[]
for n in words:
     word_split.append(stemmer.stem(n))
words = word_split
words = " ".join(words)
     
print words

s = "Useless useless2  useless3 interesting_field useless4" 
print s.split() 
print s.split(" ")
