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

for i in soup2.find_all('p') :
    print(i.text)
    
headline = soup.find_all('div', {"class" : "item_issue"})

print(headline[0].text)

for i in headline :
    print(i.text, '\n')
    
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
    
    for j in soup3.find_all('p') :
        print(j.text)
        
f = open('links.txt', 'w')
for i in soup.find_all('div', {"class" : "item_issue"}) :
    f.write(i.find_all('a')[0].get('href')+'\n')
    
f.close()

article1 = 'https://news.v.daum.net/v/20220329122101265'

soup = bs(ur.urlopen(article1).read(), 'html.parser')

f=open('article_1.txt', 'w', encoding='utf-8')

for i in soup.find_all('p') :
    f.write(i.text)
    
f.close()

url = 'https://news.v.daum.net/v/20220329111302294'
soup = bs(ur.urlopen(url).read(),'html.parser')
f = open('article_total.txt','w')
for i in soup.find_all('div',{"class" : "item_issue"}) :
    try :
        f.write(i.text + '\n')
        f.write(i.find_all('a')[0].get('href') + '\n')
        soup2 = bs(ur.urlopen(i.find_all)[0].get('href').read(),'html.parser')
        
        for j in soup2.find_all('p') :
            f.write(j.text)
        
    except :
        pass
f.close()

