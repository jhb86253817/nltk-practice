import nltk
import pprint

#split data into two parts
text = nltk.corpus.nps_chat.words()
cut = int(0.9 * len(text))
training_data, test_data = text[:cut], text[cut:]

#sort the words based on their length
words = "I turned off the spectroroute".split()
wordlens = [(len(word), word) for word in words]
wordlens.sort()
' '.join(w for (_,w) in wordlens)

#we can omit the square brackets when there is a function outside, it sometimes makes it efficient
text = "When I use a word, I acctually mean nothing..."
max(w.lower() for w in nltk.word_tokenize(text))
#the original way: max([w.lower() for w in nltk.word_tokenize(text)])

#nested list generator
m, n = 3, 7
array = [[set() for i in range(n)] for j in range(m)]
array[2][5].add('alice')
pprint.pprint(array)
