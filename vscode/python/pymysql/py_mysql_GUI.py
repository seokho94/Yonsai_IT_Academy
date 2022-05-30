import pymysql
from tkinter import *
from tkinter import messagebox

def insertData() :
    con, cur = None, None
    data1 , data2, data3, data4 = "", "", "", ""
    sql = ""
    
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')
    cur = conn.cursor()
    
    data1 = edt1.get();
    data2 = edt2.get();
    data3 = edt3.get();
    data4 = edt4.get();
    try :
        sql = "insert into userTable values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + ")"
        cur.execute(sql)
        
    except :
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
        
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    conn.commit()
    conn.close()
    
def selectData() :
    strData1, strData2, strData3, strData4 = [], [], [], []
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from userTable')
    strData1.append("사용자ID")
    strData2.append("사용자이름")
    strData3.append("이메일")
    strData4.append("출생년도")
    strData1.append("-------------")
    strData2.append("-------------")
    strData3.append("-------------")
    strData4.append("-------------")
    