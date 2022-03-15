#File read, write / input 값 받아오기
#readline.py
from numpy import unicode_
import os

f = open('C:\\Users\\YONSAI\\Documents\\GitHub/Yonsai_IT_Academy\\vscode\\python\\test.txt', "r", encoding='utf-8')
while True :
    line = f.readline()
    if not line: break
    print(line)
f.close()

with open('C:\\Users\\YONSAI\\Documents\\GitHub/Yonsai_IT_Academy\\vscode\\python\\test.txt', "w", encoding='utf-8') as f:
    f.write("Life is too short, you need python")

f = open('C:\\Users\\YONSAI\\Documents\\GitHub/Yonsai_IT_Academy\\vscode\\python\\test.txt', "r", encoding='utf-8')
line = f.readline()
print(line)
f.close()
    
