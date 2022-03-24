import usecsv as uc
import os, re, csv
os.chdir(r'C:\\Users\\YONSAI\\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\\python\\py_doit')
f = open('a.csv','r')
new = csv.reader(f)

for i in new :
    print(i)
    
a_list = []
for i in new :
    print(i)
    a_list.append(i)

f.seek(0)

for i in new :
    print(i)
    a_list.append(i)
    
print("{}".format(a_list))

ex = uc.opencsv('example2.csv')
print(ex)
a = [['구','전체','내국인','외국인'],
     ['관악구','519864','502089','17775'],
     ['강남구','547602','542498','5104'],
     ['송파구','686181','679247','6934'],
     ['강동구','428547','424235','4312']]
cs42 = open('abc.csv', 'w', newline = '')
csvobject = csv.writer(cs42, delimiter =',')
csvobject.writerows(a)
f.close()

a = [['국어','영어','수학'],
     [99,88,77]]

uc.writecsv('test.csv',a)

b = [['물리','화학','생물'],
     [70, 99, 100]]

uc.writecsv('test2.csv',b)