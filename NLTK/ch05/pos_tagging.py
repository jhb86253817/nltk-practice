import nltk

#simple pos tagger of nltk
text = nltk.word_tokenize("And now for something completely different")
print nltk.pos_tag(text)

#transform tagged strings into tuple
sent = '''
The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PP
said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/R
accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
interest/NN of/IN both/ABX governments/NNS ''/'' ./.
'''
[nltk.tag.str2tuple(t) for t in sent.split()]

#find most frequent tags in news text
from nltk.corpus import orown
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
tag_fd = nltk.FreqDist(tag for (word,tag) in brown_news_tagged)
tag_fd.keys()

#find most frequent tags before a noun
word_tag_pairs = nltk.bigrams(brown_news_tagged)
list(nltk.FreqDist(a[1] for (a,b) in word_tag_pairs if b[1]=='N'))

#find most frequent verbs in news text
wsj = nltk.corpus.treebank.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(wsj)
[word+'/'+tag for (word,tag) in word_tag_fd if tag.startswith('V')]

#build a conditional frequency distribution in which words are conditions, can find most possible tags given a word 
cfd1 = nltk.ConditionalFreqDist(wsj)
cfd1['field'].keys()
cfd1['cut'].keys()

#use tag as condition, can find most possible words given a tag
cfd2 = nltk.ConditionalFreqDist((tag,word) for (word,tag) in wsj)
cfd2['VN'].keys()

#explore the tags after 'often'
brown_lrnd_tagged = brown.tagged_words(categories='learned', simplify_tags=True)
tags = [b[1] for (a,b) in brown_lrnd_tagged if a[0]=='often']
fd = nltk.FreqDist(tags)
fd.tabulate()

#use POS to find trigrams
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if t1.startswith('V') and t2=='TO' and t3.startswith('V'):
            print w1, w2, w3
for tagged_sent in brown.tagged_sents():
    process(tagged_sent)








































