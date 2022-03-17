from cgitb import text
import tkinter as tk
from tkinter import CENTER, font
from turtle import left, width
from unittest import result

map1 = [["□" for i in range(16)]for i in range(18)]
result = ""
for i in range(len(map1)) :
    for j in range(len(map1[0])) :
        result = result + str(map1[i][j]) + " "   
    result += "\n"

maze = tk.Tk()
maze.title("Maze")
maze.geometry('400x480')
# maze.resizable(False,False)

label_timeZone = tk.Label(master=maze)
label_timeZone.pack()

label_time_text = tk.Label(master=label_timeZone, text='Time', font=('Arial',16))
label_time_text.pack(side='top')

label_time = tk.Label(master=label_timeZone, text="00:00:00", font=('Arial', 16))
label_time.pack(side='top')

bt_topArrow = tk.Button(master=maze, text="▲", font=('Arial',16), width=10)
bt_topArrow.pack()

label_center = tk.Label(master=maze)
label_center.pack()

bt_leftArrow = tk.Button(master=label_center, text="◀",font=('Arial',20), height=3)
bt_leftArrow.pack(side='left')

label_display = tk.Label(master=label_center, text=result, width=40, height=19)
label_display.pack(side='left')

bt_rightArrow = tk.Button(master=label_center, text="▶",font=('Arial',20), height=3)
bt_rightArrow.pack(side='right')

bt_bottomArrow = tk.Button(master=maze, text="▼", font=('Arial',16), width=10)
bt_bottomArrow.pack()
maze.mainloop()