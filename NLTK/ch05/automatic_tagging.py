import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
"""
#default tagger, i.e. use most possible tag to tag every token
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print default_tagger.tag(tokens)
print default_tagger.evaluate(brown_tagged_sents)

#regular expression tagger 
patterns = [
(r'.*ing$', 'VBG'), #gerunds
(r'.*ed$', 'VBD'), #simple past
(r'.*es$', 'VBZ'), #3rd singular present
(r'.*ould$', 'MD'), #models
(r'.*\'s$', 'NN$'), #possessive nouns
(r'.*s$', 'NNS'), #plural nouns
(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), #cardinal numbers
(r'.*', 'NN') #nouns(default)
]
regexp_tagger = nltk.RegexpTagger(patterns)
print regexp_tagger.tag(brown_sents[3])
print regexp_tagger.evaluate(brown_tagged_sents)

#look up tagger 
fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = fd.keys()[:100]
likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model = likely_tags)
print baseline_tagger.evaluate(brown_tagged_sents)

#integration of look up tagger and default tagger 
baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
"""
#explore the performance of the integration model, with different words size
def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(3)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title("Lookup tagger performance with varying model size")
    pylab.xlabel('model size')
    pylab.ylabel('performance')
    pylab.show()
display()
































