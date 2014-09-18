import nltk
from nltk.corpus import brown

#unigram tagging, which is similay to look up tagging but with training process
brown_tagged_sents = brown.tagged_sents(categories='news') 
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(brown_sents[2007])
print unigram_tagger.evaluate(brown_tagged_sents)

#seperate training and testing data
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print unigram_tagger.evaluate(test_sents)

#bigram tagger, performing not well when data is not big enough
bigram_tagger = nltk.BigramTagger(train_sents)
print bigram_tagger.tag(brown_sents[2007])
print unseen_sent = brown_sents[4203]
print bigram_tagger.evaluate(test_sents)

#combining taggers
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print t2.evaluate(test_sents)

#save the tagger for next time using
from cPickle import dump
output = open('t2.pkl', 'wb')
dump(t2, output, -1)
output.close()
#load the saved tagger 
from cPickle import load 
my_input = open('t2.pkl', 'rb')
tagger = load(my_input)
my_input.close()
text = "The board's action shows what free enterprise is up against in our complex maze of regulatory laws."
tokens = text.split()
print tagger.tag(tokens)


