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

def cleanMe(html):
    soup = BeautifulSoup(html, "html.parser")                                                       # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]):                                                        # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


path = 'crawled_html_pages/'
index = {}
docNum = 0
stop_words = set(stopwords.words('english'))                                                            #collection of stopwords to avoid       
for filename in os.listdir(path):                                                                       #for every doc in folder...
    collection = {}                                                                                     #all words collected from this html file
    docNum += 1                                                                                         #Start with doc 1, then 2..3..4..500
    file = codecs.open('crawled_html_pages/'+ filename,'r', 'utf-8')                                  #open the html file
    page_text = cleanMe(file)                                                                         #collect page text from html file
    tokens = nltk.word_tokenize(page_text)                                                              #tokenize page text
    filtered_sentence = [w for w in tokens if not w in stop_words]                                      #remove stopwords from page text
    filtered_sentence = []

    breakWord = ''

    for w in tokens:                                                                                    #place non-stopwords in token list                                                                                   
        if w not in stop_words:
            filtered_sentence.append(w.lower())

    for token in filtered_sentence:
        if len(token) == 1 or token == 'by':
            continue
        if checkChar(token) == False:
            continue
        if token == 'australia':
            breakWord = token
            continue
        if token == 'bangladesh' and breakWord == 'australia':
            break
        if token not in collection:
            collection[token] = 0
        collection[token] += 1            

    for token in collection:
        if token not in index:
            index[token] = ''
        index[token] = index[token] + '['+ str(docNum) + ', ' + str(collection[token]) + ']'           

f = open('index.txt', 'w')
vocab = open('uniqueWords.txt', 'w')
for term in index:
    f.write(term + ' => ' + index[term])
    vocab.write(term + '\n')
    f.write('\n')
f.close()
vocab.close()

print('Finished...')
