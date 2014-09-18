import nltk

#a simple testing for recursive descent parser
#it is a top-down method
#shortcomings: cannot deal with left-recursive, not efficient...
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
rd_parser = nltk.RecursiveDescentParser(grammar1)
sent = "Mary saw a dog".split()
for t in rd_parser.nbest_parse(sent):
    print t
