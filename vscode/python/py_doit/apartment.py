import os, re
import usecsv as uc

os.chdir(r'C:\\Users\YONSAI\\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\\python\\py_doit')
apt = uc.switch(uc.opencsv('apt_201912.csv'))
new_list = []

for i in apt :
    try :
        if i[5] > 120 and i[-7] >= 30000 and re.match('강원',i[0]):
            new_list.append([i[0], i[5], i[-7]])
            
    except : pass

uc.writecsv('over120_flower30000.csv', new_list)