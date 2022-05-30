from tkinter import *
from tkinter.simpledialog import *

window = Tk()

canvas  = Canvas(window, height = 300, width = 300)
canvas.pack()

canvas.create_line([[0,0], [70,70], [30,170]], fill="blue", width=3)
canvas.create_polygon([[100, 100], [100, 150], [150, 150], [150, 100]], fill="red")
canvas.create_text([200, 200], text="이것이 MySQL이다", font=("굴림", 15))

window.mainloop()