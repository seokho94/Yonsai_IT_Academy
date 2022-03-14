#조건문 if
from random import randint


pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    print("택시를 타고 가라")
elif card :
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
#if문을 switch처럼 사용하기
number = randint(1,5)
print(number)
if(number==1) :
    print("1번을 사용하세요")
elif(number==2) :
    print("2번을 사용하세요")
elif(number==3) :
    print("3번을 사용하세요")
elif(number==4) :
    print("4번을 사용하세요")
else :
    print("5번을 사용하세요")