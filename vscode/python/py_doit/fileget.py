import os, re, codecs

os.chdir("C:\\Users\\YONSAI\\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\python\\py_doit")
f = codecs.open('friends101.txt', 'r', encoding = 'UTF-8')
script101 = f.read()

print(script101[:100])

Line = re.findall(r'Monica:.+', script101)
print(Line[:3])

for item in Line[:3] :
    print(item)
    
f.close()
monica = ""
f = open('monica.txt', 'w', encoding = 'utf-8')
for i in Line :
    monica += i + '\n'

print(monica[:100])
f = open('monica.txt', 'w', encoding = 'utf-8')
f.write(monica)
f.close()

char = re.compile(r'[A-Z][a-z]+:')
a = [1,2,3,4,5,2,2]
set(a)
set(re.findall(char, script101))

rachel = 'Rachel:'
rachel = re.sub(':', '', rachel)
y = set(re.findall(char, script101))
z = list(y)
character = []
for i in z :
    character += [i[:-1]]
    
character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+: ',script101)))]
re.findall(r'\([A-Za-z].+[a-z|\.]\)',script101)[:6]
print(character)

f = open('friends101.txt','r')
f.read(100)
f.seek(0)

sentences = f.readlines()
sentences[:3]

for i in sentences[:20] :
    if re.match(r'[A-Z][a-z]+:', i) :
        print(i)
        
lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]

print(lines[:10])

would = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i) and re.search('would',i)]
print(would)

take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take',i)]
print(take)

newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()