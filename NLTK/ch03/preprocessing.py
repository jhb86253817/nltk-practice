#usage of tokenize
import nltk
from urllib import urlopen
"""
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw) 
text = nltk.Text(tokens)
raw = raw[raw.find("PART I"):raw.rfind("Gutenburg's Crime")]

#clean HTML
url = "http://www.weibo.com/u/1096796232/home?wvr=5"
html = urlopen(url).read()
raw = nltk.clean_html(html)
tokens = nltk.word_tokenize(raww)
text = nltk.Text(tokens)
"""
#usage of feedparser
import feedparser
llog = feedparser.parse("http://blog.csdn.net/zouxy09/")
print llog.entries
