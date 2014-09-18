#create a dictionary
pos = {'colorless':'ADJ', 'ideas':'N', 'sleep':'V', 'furiously':'ADV'}

#create a default dictionary with default value 'N'
import nltk
pos = nltk.defaultdict(lambda: 'N')
pos['colorless'] = 'ADJ'
pos['blog']
pos.items()

#substitute low-frequent words with 'UNK'
alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreqDist(alice)
v1000 = list(vocab)[:1000]
mapping = nltk.defaultdict(lambda: 'UNK')
for v in v1000:
    mapping[v] = v
alice2 = [mapping[v] for v in alice]

#updates counts of tags using defaultdict, also an important sorting method for dictionary
counts = nltk.defaultdict(int)
from nltk.corpus import brown
for (word, tag) in brown.tagged_words(categories='news'):
    counts[tag] += 1
from operator import itemgetter
[t for t,c in sorted(counts.items(), key=itemgetter(1), reverse=True)]
