import pymysql
from tkinter import *
from tkinter import messagebox

def insertData() :
    con, cur = None, None
    data1 , data2, data3, data4 = "", "", "", ""
    sql = ""
    
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')
    cur = conn.cursor()