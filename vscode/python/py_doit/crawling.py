import os, re , usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com'
html = ur.urlopen(url)

# print(html.read()[:100])

soup = bs(html.read(), 'html.parser')

quote = soup.find_all('span')

for i in quote :
    print(i.text)

for i in soup.find_all('div', {"class" : "quote"}) :
    print(i.text)
