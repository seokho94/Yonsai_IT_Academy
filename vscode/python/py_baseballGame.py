from cProfile import label
from random import *
import sys
import tkinter as tk
from tkinter import  Button, Label, messagebox as mb
from tkinter import font
from unittest import expectedFailure

#초기 설정 과정
count =0
com = [0 for i in range(4)]
result = ''
게임화면 = tk.Tk()
게임화면.title('숫자야구 게임')
게임화면.geometry('250x400')

#정답을 생성하는 과정
for i in range(len(com)):
    com[i] = randint(1,9)

#중복값 처리 과정
#각 인덱스 값을 비교하여 중복 값 확인
#중복 값이 있다면 새로운 숫자를 부여
#중복 값이 없다면 다음 인덱스로 넘어가여 진행
for i in range(len(com)):
    for j in range(len(com)):
        if i != j:
            if com[i] == com[j]:
                while True:
                    com[i] = randint(1,9)
                    if com[i] != com[j]:
                        break
    result += str(com[i])

#ball, strike 확인 함수
#숫자와 자리수가 같다면 strike++
#숫자는 같지만 자리수가 다르다면 ball++ 
def checkNum(arr) :
    ball=0
    strike=0
    global com
    for i in range(len(arr)) :
        for j in range(len(com)) :
            if(arr[i]==com[j]) :
                if(i==j) : strike +=1
                else : ball +=1
    return ball,strike

#예외처리 -> 3자리 자리수 확인
#3자리 숫자라면 clickEvent 실행
#100으로 나눴을때 몫의 범위는 1-9까지
#-> 각자리마다 1~9까지기때문에 몫의 최소값은 1
def checkData() :
    try :
        num = int(e.get())
        if(num/1000) >=1 and (num/1000) <10 :
            check = True
            checkNum = str(num)
            for i in range(len(checkNum)) :
                if(checkNum[i]=='0') :
                    check = False
            if check :
                clickEvent(checkNum)
            else : 
                mb.showinfo(title='입력 오류',message='0을 제외한 4자리 숫자만 입력해주세요.')
        else :
            mb.showinfo(title='입력 오류',message='0을 제외한 4자리 숫자만 입력해주세요.')
    except :
        mb.showinfo(title='입력 오류',message='0을 제외한 4자리 숫자만 입력해주세요.')
        
#버튼 클릭시 3자리 숫자를 받아 처리하는 함수
#count 값 1씩 증가 남은 기회를 출력
#남은 기회 = 최초 기회 - count
#기회가 남았다면 입력 값 결과 출력
#if 3strike 라면 '승 리' 메세지 출력
#기회가 없고 3strike가 아니라면
#-> 결과 값 출력
#->'패 배' 메세지 출력
def clickEvent(num):
    global count
    userNum = num
                
    count += 1
    레이블2.config(text='남은 기회 : {}'.format(7-count))
    lst = []

    for i in userNum:
        lst.append(i)
    lst = [int (i) for i in lst]

    ball, strike = checkNum(lst)

    if count < 7:
        if(strike==4) :
            레이블1.config(text=result)
            mb.showinfo(title='결과',message='승 리')
        else :
            label = Label(게임화면, text=userNum+' | {}B {}S'.format(ball, strike),font=('Arial',15))
            label.pack()
    else:
        if(strike==4) :
            label = Label(게임화면, text=userNum+' | {}B {}S'.format(ball, strike),font=('Arial',15))
            label.pack()
            레이블1.config(text=result)
            mb.showinfo(title='결과',message='승 리')
            sys.exit()
        else :
            label = Label(게임화면, text=userNum+' | {}B {}S'.format(ball, strike),font=('Arial',15))
            label.pack()
            레이블1.config(text=result)
            mb.showinfo(title='결과',message='패 배')
            sys.exit()

#타겟 넘버 레이블 -> 게임 종료시 타겟 넘버 공개
레이블1 = tk.Label(master=게임화면,text= '????',font = ('Arial',30))
레이블1.pack()
#남은 기회를 출력해주는 레이블 -> 초기 값 5 , 남은 기회 = 초기 값 -count
레이블2 = tk.Label(master=게임화면,text='남은 기회 : 7',font=('Arial',20))
레이블2.pack()
#입력 값에 대한 안내를 해주는 레이블
레이블3 = tk.Label(master=게임화면,text= '4자리 숫자를 입력하세요.',font = ('Arial',13))
레이블3.pack()
#입력 값을 받아오는 Entry
e = tk.Entry(master=게임화면,font=('Arial',16))
e.pack()
e.insert(0,'')
#Entry 값을 처리해주는 버튼, 클릭시 checkData 함수 실행(command=checkData)
버튼1 = tk.Button(master=게임화면,text='출력',font=('Arial',13),command=checkData)
버튼1.pack()
#게임 실행
게임화면.mainloop()