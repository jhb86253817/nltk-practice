#gender identification, using naive bayes
def gender_features(word):
    return {'last_letter': word[-1]}
import nltk
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] + 
        [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print classifier.classify(gender_features('Neo'))
print classifier.classify(gender_features('Trinity'))
print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(5)
#when data is big, such lists will cost much memory
#using 'apply_features' can return an object which act like list but not store all the data in memory
from nltk.classify import apply_features
train_set = apply_features(gender_features, names[500:])
test_set = apply_features(gender_features, names[:500])

#error analysis, seperating data into three: train_set, devtest_set, test_set 
train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]
train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)
#observe the wrong predictions
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))
#printing results
for (tag, guess, name) in sorted(errors):
    print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

#define new gender_features, which also extract the last two letters of names 
def gender_features2(word):
    return {'suffix1': word[-1:], 'suffix2': word[-2:]}
train_set2 = [(gender_features2(n), g) for (n,g) in train_names]
devtest_set2 = [(gender_features2(n), g) for (n,g) in devtest_names]
test_set2 = [(gender_features2(n), g) for (n,g) in test_names]
classifier2 = nltk.NaiveBayesClassifier.train(train_set2)
print nltk.classify.accuracy(classifier2, devtest_set2)
    

print nltk.classify.accuracy(classifier2, test_set2)
