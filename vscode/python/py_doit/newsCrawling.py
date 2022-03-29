import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir(r'C:\\Users\\YONSAI\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\\python\\py_doit')
news = 'https://news.daum.net/'
soup = bs(ur.urlopen(news).read(), 'html.parser')

for i in soup.find_all('div', {"class" : "item_issue"}) :
    print(i.find_all('a')[0].get('href'))

article1 = 'https://news.v.daum.net/v/20220329102612815'
soup2 = bs(ur.urlopen(article1).read(), 'html.parser')