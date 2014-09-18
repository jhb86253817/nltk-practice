from nltk.book import *

#find the word and its context
text1.concordance("morning")

#find similar word that in the same context
text1.similar("morning")
text2.similar("morning")

#find similar words that in the same context
text1.common_contexts(["morning", "bed"])

#plot dispersion of some words
text1.dispersion_plot(["morning","bed","eat","go","coffee"])

#randomly generate some text based on the language model
text1.generate()

#the length of total words and the length of unique words
len(text1); len(set(text1))

#count the word
text1.count("morning")

#connect the list of words
sent1 + sent2

#append
sent1.append("nooooo")

#find the first index the word appear
text1.index("morning")

#transform words list to string
' '.join(["good", "morning"])

#split string into words list
"good morning".split()


















