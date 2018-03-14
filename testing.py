from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs





def cleanMe(html):
    soup = BeautifulSoup(html, "html.parser") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
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


path = 'F:\GitHub\WebCrawler\web_crawler\crawled_html_pages'
for filename in os.listdir(path):                                                                       #for every doc in folder...
    file = codecs.open('F:\GitHub\WebCrawler\web_crawler\crawled_html_pages\\'+ filename,'r', 'utf-8')  #open the html file
    cleaned = cleanMe(file)                                                                  #collect page text from html file
    print(cleaned)
    break
