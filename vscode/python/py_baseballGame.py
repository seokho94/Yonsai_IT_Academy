from cProfile import label
from random import *
import tkinter as tk
from tkinter import  Button, Label, messagebox as mb
from tkinter import font

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

def clickEvent():
    global cunt
    cunt += 1
    레이블2.config(text='남은 기회 : {}'.format(5-cunt))
    userNum = e.get()
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
        else :
            label = Label(게임화면, text=userNum+' | {}B {}S'.format(ball, strike),font=('Arial',15))
            label.pack()
            레이블1.config(text=result)
            mb.showinfo(title='결과',message='패 배')

레이블1 = tk.Label(master=게임화면,text= '???',font = ('Arial',30))
레이블1.pack()

레이블2 = tk.Label(master=게임화면,text='남은 기회 : 5',font=('Arial',20))
레이블2.pack()

레이블3 = tk.Label(master=게임화면,text= '3자리 숫자를 입력하세요.',font = ('Arial',13))
레이블3.pack()

e = tk.Entry(master=게임화면,font=('Arial',16))
e.pack()
e.insert(0,'')

버튼1 = tk.Button(master=게임화면,text='출력',font=('Arial',13),command=clickEvent)
버튼1.pack()

게임화면.mainloop()