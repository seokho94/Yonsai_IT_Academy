import tkinter as tk
from turtle import color

rainbow = tk.Tk()
rainbow.title('rainbow')
rainbow.geometry('340x420')
color_arr = [[0 for col in range(21)]for col in range(12)]
count = 7 

def check_arr() :
    global color_arr
    for i in range(len(color_arr)) :
        result = ""
        for j in range(len(color_arr[0])) :
            result += "{} ".format(color_arr[i][j])
        
        print(result,"\n")

def fill_color(idx_x, idx_y) :
    global color_arr
    color_arr[idx_y][idx_x] = count

def find_center_idx(idx_x, idx_y) :
    fill_color(idx_x,idx_y)    

def find_left_idx(idx_x, idx_y) :
    while True :
        fill_color(idx_x,idx_y)
        idx_x-=1
        idx_y+=1
        if(idx_x<0 or idx_y>11) :
            break

def find_right_idx(idx_x, idx_y) :
    while True :
        fill_color(idx_x,idx_y)
        idx_x+=1
        idx_y+=1
        if(idx_x>20 or idx_y>11) :
            break

def making_rainbow() :
    global count
    center_Y = 2
    center_X = 10
    left_Y = 2
    left_X = 9
    right_Y =2
    right_X = 11
    for i in range(7):
        find_center_idx(center_X, center_Y)
        find_left_idx(left_X, left_Y)
        find_right_idx(right_X,right_Y)
        center_Y+=1
        left_Y+=1
        right_Y+=1
        count-=1
    # check_arr()

#row0
label1 = tk.Label(master=rainbow, width=2, height=2)
label1.grid(row=0, column=0)

label2 = tk.Label(master=rainbow, width=2, height=2)
label2.grid(row=0, column=1)

label3 = tk.Label(master=rainbow, width=2, height=2)
label3.grid(row=0, column=2)

label4 = tk.Label(master=rainbow, width=2, height=2)
label4.grid(row=0, column=3)

label5 = tk.Label(master=rainbow, width=2, height=2)
label5.grid(row=0, column=4)

label6 = tk.Label(master=rainbow, width=2, height=2)
label6.grid(row=0, column=5)

label7 = tk.Label(master=rainbow, width=2, height=2)
label7.grid(row=0, column=6)

label8 = tk.Label(master=rainbow, width=2, height=2)
label8.grid(row=0, column=7)

label9 = tk.Label(master=rainbow, width=2, height=2)
label9.grid(row=0, column=8)

label10 = tk.Label(master=rainbow, width=2, height=2)
label10.grid(row=0, column=9)

label11 = tk.Label(master=rainbow, width=2, height=2)
label11.grid(row=0, column=10)

label12 = tk.Label(master=rainbow, width=2, height=2)
label12.grid(row=0, column=11)

label13 = tk.Label(master=rainbow, width=2, height=2)
label13.grid(row=0, column=12)

label14 = tk.Label(master=rainbow, width=2, height=2)
label14.grid(row=0, column=13)

label15 = tk.Label(master=rainbow, width=2, height=2)
label15.grid(row=0, column=14)

label16 = tk.Label(master=rainbow, width=2, height=2)
label16.grid(row=0, column=15)

label17 = tk.Label(master=rainbow, width=2, height=2)
label17.grid(row=0, column=16)

label18 = tk.Label(master=rainbow, width=2, height=2)
label18.grid(row=0, column=17)

label19 = tk.Label(master=rainbow, width=2, height=2)
label19.grid(row=0, column=18)

label20 = tk.Label(master=rainbow, width=2, height=2)
label20.grid(row=0, column=19)

label21 = tk.Label(master=rainbow, width=2, height=2)
label21.grid(row=0, column=20)

#row1
label22 = tk.Label(master=rainbow, width=2, height=2)
label22.grid(row=1, column=0)

label23 = tk.Label(master=rainbow, width=2, height=2)
label23.grid(row=1, column=1)

label24 = tk.Label(master=rainbow, width=2, height=2)
label24.grid(row=1, column=2)

label25 = tk.Label(master=rainbow, width=2, height=2)
label25.grid(row=1, column=3)

label26 = tk.Label(master=rainbow, width=2, height=2)
label26.grid(row=1, column=4)

label27 = tk.Label(master=rainbow, width=2, height=2)
label27.grid(row=1, column=5)

label28 = tk.Label(master=rainbow, width=2, height=2)
label28.grid(row=1, column=6)

label29 = tk.Label(master=rainbow, width=2, height=2)
label29.grid(row=1, column=7)

label30 = tk.Label(master=rainbow, width=2, height=2)
label30.grid(row=1, column=8)

label31 = tk.Label(master=rainbow, width=2, height=2)
label31.grid(row=1, column=9)

label32 = tk.Label(master=rainbow, width=2, height=2)
label32.grid(row=1, column=10)

label33 = tk.Label(master=rainbow, width=2, height=2)
label33.grid(row=1, column=11)

label34 = tk.Label(master=rainbow, width=2, height=2)
label34.grid(row=1, column=12)

label35 = tk.Label(master=rainbow, width=2, height=2)
label35.grid(row=1, column=13)

label36 = tk.Label(master=rainbow, width=2, height=2)
label36.grid(row=1, column=14)

label37 = tk.Label(master=rainbow, width=2, height=2)
label37.grid(row=1, column=15)

label38 = tk.Label(master=rainbow, width=2, height=2)
label38.grid(row=1, column=16)

label39 = tk.Label(master=rainbow, width=2, height=2)
label39.grid(row=1, column=17)

label40 = tk.Label(master=rainbow, width=2, height=2)
label40.grid(row=1, column=18)

label41 = tk.Label(master=rainbow, width=2, height=2)
label41.grid(row=1, column=19)

label42 = tk.Label(master=rainbow, width=2, height=2)
label42.grid(row=1, column=20)

#row2

making_rainbow()

rainbow.mainloop()