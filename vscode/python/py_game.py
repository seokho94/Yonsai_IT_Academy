import tkinter as tk
from random import *

게임화면  = tk.Tk()
게임화면.title('묵찌빠 게임')
게임화면.geometry("250x350")

레이블1 = tk.Label(master= 게임화면, text='컴퓨터', font=('Arial',15))
레이블1.place(x=0, y=0, width=150, height=50)

레이블2 = tk.Label(master= 게임화면, text='나', font=('Arial',15))
레이블2.place(x=200, y=0, width=150, height=50)

레이블3 = tk.Label(master= 게임화면, text='-', font=('Arial',30), bg="red", fg="white")
레이블3.place(x=0, y=50, width=150, height=150)

레이블4 = tk.Label(master= 게임화면, text='VS', font=('Arial',20))
레이블4.place(x=150, y=50, width=50, height=150)

버튼1 = tk.Button(master = 게임화면, text='묵', font=('Arial', 10), command=lambda:컴퓨터선택(1))
버튼1.place(x=200, y=50, width=150, height=50)

버튼2 = tk.Button(master = 게임화면, text='찌', font=('Arial', 10), command=lambda:컴퓨터선택(2))
버튼2.place(x=200, y=100, width=150, height=50)

버튼3 = tk.Button(master = 게임화면, text='빠', font=('Arial', 10), command=lambda:컴퓨터선택(3))
버튼3.place(x=200, y=150, width=150, height=50)

from tkinter import messagebox as mb

def 컴퓨터선택(사용자의선택) :
    global 레이블3
    묵찌빠 = {1:'묵', 2:'찌', 3:'빠'}
    
    컴퓨터의선택 = randint(1, 3)
    레이블3.config(text = 묵찌빠[컴퓨터의선택])
    
    if 컴퓨터의선택 == 사용자의선택:
        mb.showinfo(title = '결과', message = '당신이 이겼습니다!')
        레이블3.config(text = '-')
        
게임화면.mainloop()