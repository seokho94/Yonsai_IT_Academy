from cgitb import text
from doctest import master
import tkinter as tk
import time
import sys
from tkinter import font

from setuptools import Command

def start_time() :
    timeCheck = time.strftime('%H %M %S')
    timeArr = timeCheck.split(" ")
    sign = 'AM'
    if(int(timeArr[0]) > 12 and int(timeArr[0]) < 24) :
        sign = change_sign(True)
        timeArr[0] = change_hour(timeArr[0])
    elif int(timeArr[0]) == 12 :
        sign = change_sign(True)
    elif int(timeArr[0]) == 24 :
        sign = change_sign(False)
        change_Date()
    else :
        sign = change_sign(False)
    label2.config(text="{} : {} : {}".format(timeArr[0],timeArr[1],timeArr[2])+sign)
    infoDate = time.strftime('%Y %m %d %A')
    chage_day = {'Monday':'(월)', 'TuesDay':'(화)', 'Wednesday' : '(수)', 'Thursday' : '(목)', 'Friday' : '(금)', 'Saturday' : '(토)', 'Sunday' : '(일)'}
    dateArr = infoDate.split(" ")
    day = chage_day[dateArr[3]]
    dateArr[3] = day
    label3.config(text="{}년 {}월 {}일 {}".format(dateArr[0],dateArr[1],dateArr[2],dateArr[3]))
    update_time()

#시간 업데이트
def update_time() :
    timeCheck = time.strftime('%H %M %S')
    timeArr = timeCheck.split(" ")
    sign = 'AM'
    if(int(timeArr[0]) > 12 and int(timeArr[0]) < 24) :
        sign = change_sign(True)
        timeArr[0] = change_hour(timeArr[0])
    elif int(timeArr[0]) == 12 :
        sign = change_sign(True)
    elif int(timeArr[0]) == 24 :
        sign = change_sign(False)
        change_Date()
    else :
        sign = change_sign(False)
    label2.config(text="{} : {} : {}".format(timeArr[0],timeArr[1],timeArr[2])+sign)
    label2.after(100, update_time)
    #레이블 텍스트 값 변경
    
#시간에 따라 Am/ Pm 변환
def change_sign(sign) :
    if(sign) :
        return 'PM'
    else :
        return 'AM'

#24시간을 12시간으로 변경
def change_hour(h) :
    hour = int(h)
    hour -= 12
    return hour

#00시가 되었을때 날짜 변경
def change_Date() :
    infoDate = time.strftime('%Y %m %d %A')
    chage_day = {'Monday':'(월)', 'TuesDay':'(화)', 'Wednesday' : '(수)', 'Thursday' : '(목)', 'Friday' : '(금)', 'Saturday' : '(토)', 'Sunday' : '(일)'}
    dateArr = infoDate.split(" ")
    day = chage_day[dateArr[3]]
    dateArr[3] = day
    label3.config(text="{}년 {}월 {}일 {}".format(dateArr[0],dateArr[1],dateArr[2],dateArr[3]))

def change_default() :
    clock.config(bg='#f0f0f0')
    label1.config(bg='#f0f0f0')
    label2.config(bg='#f0f0f0')
    label3.config(bg='#f0f0f0')
    label1.config(bg='#f0f0f0')
    label2.config(bg='#f0f0f0')
    label3.config(bg='#f0f0f0')
    label4.config(bg='#f0f0f0')
    bt_default.config(bg='#f0f0f0')
    bt_white.config(bg='#f0f0f0')
    bt_black.config(bg='#f0f0f0')
    bt_default.config(fg='black')
    bt_white.config(fg='black')
    bt_black.config(fg='black')
    label1.config(fg='black')
    label2.config(fg='black')
    label3.config(fg='black')

def change_white() :
    clock.config(bg='white')
    label1.config(bg='white')
    label2.config(bg='white')
    label3.config(bg='white')
    label1.config(bg='white')
    label2.config(bg='white')
    label3.config(bg='white')
    label4.config(bg='white')
    bt_default.config(bg='white')
    bt_white.config(bg='white')
    bt_black.config(bg='white')
    bt_default.config(fg='black')
    bt_white.config(fg='black')
    bt_black.config(fg='black')
    label1.config(fg='black')
    label2.config(fg='black')
    label3.config(fg='black')
    
def change_black() :
    clock.config(bg='black')
    label1.config(bg='black')
    label2.config(bg='black')
    label3.config(bg='black')
    label4.config(bg='black')
    bt_default.config(bg='black')
    bt_white.config(bg='black')
    bt_black.config(bg='black')
    label1.config(fg='white')
    label2.config(fg='white')
    label3.config(fg='white')
    bt_default.config(fg='white')
    bt_white.config(fg='white')
    bt_black.config(fg='white')
        
clock = tk.Tk()
clock.title('Clock')
clock.geometry('400x140')

label1 = tk.Label(master=clock, text='현재 시간', font = ('Arial', 20))
label1.pack()

label2 = tk.Label(master=clock, text=time.strftime('%H' + ':' + '%M' + ':' + '%S'), font=('Arial', 24))
label2.pack()

label3 = tk.Label(master=clock, text="", font=('Arial', 16))
label3.pack()

label4 = tk.Label(master=clock, height="20")
label4.pack()

bt_default = tk.Button(master=label4, text="Default", font=('Arial', 12), command=change_default)
bt_default.pack(side='left')

bt_white = tk.Button(master=label4, text="White", font=('Arial', 12), command=change_white)
bt_white.pack(side='left')

bt_black = tk.Button(master=label4, text="Black", font=('Arial', 12), command=change_black)
bt_black.pack(side='left')

start_time()

clock.mainloop()
