from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs


        
f = codecs.open("F:\GitHub\WebCrawler\web_crawler\crawled_html_pages/3D audio effect - Wikipedia.html", 'r', 'utf-8')

soup = BeautifulSoup(f, 'html.parser')
page_text = soup.get_text()
stop_words = set(stopwords.words('english'))

index = {}
docNum = 0

c = {}
tokens = nltk.word_tokenize(page_text)

filtered_sentence = [w for w in tokens if not w in stop_words]
filtered_sentence = []

for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

test = {}
for token in filtered_sentence:
    if not token in test:
        test[token] = 0
    test[token] += 1
    

for token in test:
    if token not in index:
        index[token] = test[token]

print(index)
#print(page_text)
