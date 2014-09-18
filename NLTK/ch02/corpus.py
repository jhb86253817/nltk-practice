#import gutenberg corpus and transform it to certain type of text
import nltk
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
emma = nltk.Text(emma)
emma.concordance("morning")

#compute the average length of word, sentence and word diversity
from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

#tests of brown corpus, with many texts from different sources 
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print m + ':', fdist[m],

#generate random texts using bigram 
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
generate_model(cfd, "living")

#calculate the fraction of the words that are not stopwords
from nltk.corpus import stopwords
def content_fraction(text):
    stopwords = stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)




















