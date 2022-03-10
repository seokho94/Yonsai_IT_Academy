from random import *
import time

def 원하는정수값받기(질문):
    while True:
        try:
            입력값 = int(input(질문))
            if 입력값 >=1 and 입력값 <=3:
                break
            else:
                print('1에서 3사이의 숫자만 입력하세요')
        except:
            print('잘못 입력했습니다. 숫자를 입력하세요')

    return 입력값
   
print('게임 시작!')

게임수 = 0

while True:
   
    입력값 = 원하는정수값받기('[참가자] 숫자 몇 개를 부를 건가요? (1~3):')
       
    for 숫자 in range(입력값):
        print('{}!'.format(게임수 + 1 + 숫자))
   
    게임수 = 게임수 + 입력값 #1  #2  #3
   
    if(게임수 >= 31):
        break
   
    time.sleep(2)
   
    입력값 = randint(1,3)
    print('[컴퓨터] 숫자 몇 개를 부를 건가요? (1~3)'.format(입력값))
   
    for 숫자 in range(입력값):
        print('{}!'.format(게임수 + 1 + 숫자))
       
    게임수 = 게임수 + 입력값 #4  #5  #6
   
    if(게임수 >=31):
        break
print('벌칙 당첨!')