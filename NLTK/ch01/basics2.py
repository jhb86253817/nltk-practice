from nltk.book import *

#frequency distribution of a text
fdist1 = FreqDist(text1)
vocabulary1 = fdist1.keys()
vocabulary1[:50]
fdist1['whale']
fdist1.plot(50, cumulative = True)

#find words with more than 15 characters
V = set(text1)
long_words = [w for w in V if len(w)>15]

#find words with more than 7 charaters and appears more than 7 times
[w for w in V if len(w)>7 and fdist1[w]>7]

#get the bigram list of a text
bigrams(["call", "me", "maybe"])

#get collocations of a text, which means meaningful bigrams
text1.collocations()

#get the frequency distribution of the length of words
fdist = FreqDist([len(w) for w in text1])
fdist.keys
fdist.items()
fdist1.max()
fdist.freq(3)

#select words that satisfy the condition
[w for w in set(text1) if w.endswith('ableness')]
[w for w in set(text1) if 'gnt' in w]
