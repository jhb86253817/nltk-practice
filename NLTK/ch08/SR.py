import nltk

#a simple testing for shift reduce parser 
#it is a bottom up method 
grammar1 = nltk.parse_cfg("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | DEt N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
""")
sr_parser = nltk.ShiftReduceParser(grammar1)
sent = "Mary saw a dog".split()
print sr_parser.parse(sent)

