from sympy import ilcm
import usecsv as uc
import os, re
os.chdir(r'C:\\Users\\YONSAI\\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\\python\\py_doit') 
total  = uc.opencsv('popSeoul.csv')
    
newPop = uc.switch(total)
print(newPop[:4])

for i in newPop :
    foreign = 0
    try :
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        print(i[0], foreign)
    except :
        pass
    
new = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in newPop :
    foreign = 0
    try :
        foreign = round(i[2] / (i[1]+i[2])*100, 1)
        if foreign >3 :
            new.append([i[0],i[1],i[2],foreign])
        
    except :
        pass

uc.writecsv('newPop.csv', new)