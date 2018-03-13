from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs

strw = ' 1234Hello'
str1 = 'str:d' + strw

tokens = nltk.word_tokenize(str1)
'''
for token in tokens:
    for char in token:
        if (0 <= ord(char) and ord(char) <= 64) or (91 <= ord(char) and ord(char) <= 96) or (123 <= ord(char) and ord(char) <= 126):
           print(char)
           break
        else:
            print(char)
            continue
    break

print(ord('s'))
'''
def checkChar(token):
    for char in token:
        if (0 <= ord(char) and ord(char) <= 64) or (91 <= ord(char) and ord(char) <= 96) or (123 <= ord(char) and ord(char) <= 126):
           return False
        else:
            continue
    return True

print(checkChar(str1))
