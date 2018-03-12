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



#print(page_text)
