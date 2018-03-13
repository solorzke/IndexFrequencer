from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs


for filename in os.listdir('F:\GitHub\WebCrawler\web_crawler\crawled_html_pages'):
    file = codecs.open('F:\GitHub\WebCrawler\web_crawler\crawled_html_pages\\'+ filename,'r', 'utf-8')
    soup = BeautifulSoup(file, 'html.parser')
    title = soup.title.string
    print(title)

