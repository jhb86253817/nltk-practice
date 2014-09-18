import math, nltk

#calculate entropy for a list of labels
def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])
print entropy(['male', 'femal', 'male', 'male'])
