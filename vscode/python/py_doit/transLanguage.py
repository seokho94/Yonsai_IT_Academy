import re, usecsv, os
import usecsv as uc
os.chdir('C:\\Users\\YONSAI\\Documents\\GitHub\\Yonsai_IT_Academy\\vscode\\python\\py_doit')

English = 'She is a vegetarian. She does not eat meat. She thinks that animals should not be killed. It is hard for her to hang out with people. Many people like to eat meat. She told his parents not to have meat. They laughed at her. She realized they couldn\'t give up meat'

Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽이지 말아야한다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다. 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃었다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'

Korean_list = re.split('\.', Korean)

English_list = re.split('\.', English)

total = []

for i in range(len(English_list)) :
    total.append([English_list[i], Korean_list[i]])
    
uc.writecsv('Korean_English.csv', total)