import re, nltk
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

#searching for words that end with 'ed'
[w for w in wordlist if re.search('ed$', w)]

#searching for words with 8 letters that 3rd letter is j and 6th letter is t
[w for w in wordlist if re.search('^..j..t..$', w)]

#counting times of 'email' or 'e-mail', '?' matches one or not
sum(1 for w in wordlist if re.search('^e-?mail$', w))

#T9 system
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]

#example for '+', '+' matches one or more
[w for w in wordlist if re.search('^m+i+n+e+$', w)]
[w for w in wordlist if re.search('^[ha]+$', w)]

#example for '*', '*' matches zero or more
[w for w in wordlist if re.search('^m*i*n*e*$', w)]
[w for w in wordlist if re.search('^[ha]*$', w)]

#usage of '^' when it appears inside the square parenthesis, and it means not including the letters in parenthesis
[w for w in wordlist if re.search('^[^aeiouAEIOU]+$', w)]

#usage of '{}', means the times of repetation
[w for w in wordlist if re.search('^[0-9]{4}$', w)]

#usage of '|', means choose one among them
[w for w in wordlist if re.search('(ing|ed)$', w)]

#a simple function for stemming
def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem
