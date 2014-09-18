import nltk

#an existing function for NE classification
sent = nltk.corpus.treebank.tagged_sents()[22]
print nltk.ne_chunk(sent, binary=True)
print nltk.ne_chunk(sent)
