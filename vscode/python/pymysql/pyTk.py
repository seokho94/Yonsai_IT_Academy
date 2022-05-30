from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger

def func_open() :
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit() :
    window.quit()
    window.destroy()

window = Tk()

btnList = [None] * 3

label1 = Label(window, text="This is MySQL을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부 중입니다.", bg = "magenta", width=20, height=5)

label1.pack()
label2.pack()
label3.pack()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack()
button2.pack()
button3.pack()

for i in range(0,3) :
    btnList[i] = Button(window, text="버튼"+str(i+4))

for btn in btnList :
    btn.pack(side=RIGHT, fill=X, padx=10, pady=10)

upFrame = Frame(window)
upFrame.pack()
downFrame = Frame(window)
downFrame.pack()

editBox = Entry(upFrame, width = 10, bg = 'green')
editBox.pack(padx = 20, pady = 20)

listbox = Listbox(downFrame, bg = 'yellow')
listbox.pack()

listbox.insert(END, "하나")
listbox.insert(END, "둘")

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

label7 = Label(window, text="입력된 값")
label7.pack()


value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue = 1, maxvalue = 6)

label7.configure(text=str(value))

window.mainloop()
