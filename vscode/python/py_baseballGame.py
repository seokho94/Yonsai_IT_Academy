from cProfile import label
from random import *
import sys
import tkinter as tk
from tkinter import  Button, Label, messagebox as mb
from tkinter import font
from unittest import expectedFailure

cunt =0
com = ['','','']
result = ''
게임화면 = tk.Tk()
게임화면.title('숫자야구 게임')
게임화면.geometry('250x400')

for i in range(3):
    com[i] = randint(1,9)


for i in range(3):
    for j in range(len(com)):
        if i != j:
            if com[i] == com[j]:
                while True:
                    com[i] = randint(1,9)
                    if com[i] != com[j]:
                        break
    result += str(com[i])

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

def checkData() :
    try :
        num = int(e.get())
        if(num/100) >=1 and (num/100) <=9 :
            clickEvent(str(num))
        else :
            mb.showinfo(title='입력 오류',message='3자리 숫자만 입력해주세요.')
    except :
        mb.showinfo(title='입력 오류',message='3자리 숫자만 입력해주세요.')
        
def clickEvent(num):
    global cunt
    userNum = num
                
    cunt += 1
    레이블2.config(text='남은 기회 : {}'.format(5-cunt))
    lst = []

    for i in userNum:
        lst.append(i)
    lst = [int (i) for i in lst]

    ball, strike = checkNum(lst)

    if cunt < 5:
        if(strike==3) :
            레이블1.config(text=result)
            mb.showinfo(title='결과',message='승 리')
        else :
            label = Label(게임화면, text=userNum+' | {}B {}S'.format(ball, strike),font=('Arial',15))
            label.pack()
    else:
        if(strike==3) :
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

레이블1 = tk.Label(master=게임화면,text= '???',font = ('Arial',30))
레이블1.pack()

레이블2 = tk.Label(master=게임화면,text='남은 기회 : 5',font=('Arial',20))
레이블2.pack()

레이블3 = tk.Label(master=게임화면,text= '3자리 숫자를 입력하세요.',font = ('Arial',13))
레이블3.pack()

e = tk.Entry(master=게임화면,font=('Arial',16))
e.pack()
e.insert(0,'')

버튼1 = tk.Button(master=게임화면,text='출력',font=('Arial',13),command=checkData)
버튼1.pack()

게임화면.mainloop()