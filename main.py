from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs

def checkChar(token):
    for char in token:
        if (0 <= ord(char) and ord(char) <= 64) or (91 <= ord(char) and ord(char) <= 96) or (123 <= ord(char)):
           return False
        else:
            continue
    return True

path = 'F:\GitHub\WebCrawler\web_crawler\crawled_html_pages'
index = {}
docNum = 0
for filename in os.listdir(path):                                                                       #for every doc in folder...
    collection = {}                                                                                     #all words collected from this html file
    docNum += 1                                                                                         #Start with doc 1, then 2..3..4..500
    file = codecs.open('F:\GitHub\WebCrawler\web_crawler\crawled_html_pages\\'+ filename,'r', 'utf-8')  #open the html file
    soup = BeautifulSoup(file, 'html.parser')                                                           #parse the html
    page_text = soup.get_text()                                                                         #collect page text from html file
    stop_words = set(stopwords.words('english'))                                                        #collection of stopwords to avoid       
    tokens = nltk.word_tokenize(page_text)                                                              #tokenize page text
    filtered_sentence = [w for w in tokens if not w in stop_words]                                      #remove stopwords from page text
    filtered_sentence = []

    for w in tokens:                                                                                    #place non-stopwords in token list                                                                                   
        if w not in stop_words:
            filtered_sentence.append(w.lower())

    for token in filtered_sentence:
        if checkChar(token) == False:
            continue
        if token not in collection:
            collection[token] = 0
        collection[token] += 1            

    for token in collection:
        if token not in index:
            index[token] = ''
        index[token] = index[token] + '['+ str(docNum) + ', ' + str(collection[token]) + ']'
    if docNum == 3:
        break
    else:
        continue            
        
for k in index:
    print(k + ' '+ index[k])
