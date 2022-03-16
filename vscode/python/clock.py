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
    lable2.config(text="{} : {} : {}".format(timeArr[0],timeArr[1],timeArr[2])+sign)
    infoDate = time.strftime('%Y %m %d %A')
    chage_day = {'Monday':'(월)', 'TuesDay':'(화)', 'Wednesday' : '(수)', 'Thursday' : '(목)', 'Friday' : '(금)', 'Saturday' : '(토)', 'Sunday' : '(일)'}
    dateArr = infoDate.split(" ")
    day = chage_day[dateArr[3]]
    dateArr[3] = day
    lable3.config(text="{}년 {}월 {}일 {}".format(dateArr[0],dateArr[1],dateArr[2],dateArr[3]))
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
    lable2.config(text="{} : {} : {}".format(timeArr[0],timeArr[1],timeArr[2])+sign)
    lable2.after(500, update_time)
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
    lable3.config(text="{}년 {}월 {}일 {}".format(dateArr[0],dateArr[1],dateArr[2],dateArr[3]))

        
clock = tk.Tk()
clock.title('Clock')
clock.geometry('400x140')

lable1 = tk.Label(master=clock, text='현재 시간', font = ('Arial', 20))
lable1.pack()

lable2 = tk.Label(master=clock, text=time.strftime('%H' + ':' + '%M' + ':' + '%S'), font=('Arial', 24))
lable2.pack()

lable3 = tk.Label(master=clock, text="", font=('Arial', 16))
lable3.pack()

start_time()

clock.mainloop()
