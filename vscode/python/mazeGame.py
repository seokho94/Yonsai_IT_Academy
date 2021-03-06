from cProfile import label
from cgitb import text
from random import randint
from re import X
import tkinter as tk
from tkinter import CENTER, font, messagebox as mb
from turtle import Screen, left, onkeypress, right, title, width
from unittest import result
import sys
import time
import datetime
import keyboard as kb
from sympy import true

#map size 16 *18 도착지점 인덱스 [15][17]
map1 = [["●", "■", "□", "□", "□", "■", "□", "□", "□", "□", "■", "■", "■", "■", "■", "■"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "□", "■", "□", "□", "□", "□", "□"],
        ["□", "■", "□", "■", "□", "□", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "□", "□", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "□", "□", "■", "□", "■", "□", "■", "□", "□", "□", "□", "■", "□", "■", "□"],
        ["■", "□", "■", "■", "□", "■", "□", "■", "□", "■", "■", "■", "■", "□", "■", "□"],
        ["□", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□", "□", "□", "□", "■", "□"],
        ["□", "■", "■", "■", "□", "■", "■", "■", "□", "■", "□", "■", "■", "■", "□", "□"],
        ["□", "□", "□", "■", "□", "□", "□", "□", "□", "■", "□", "□", "■", "■", "□", "■"],
        ["■", "■", "□", "■", "■", "■", "□", "□", "■", "□", "■", "□", "■", "□", "□", "■"],
        ["□", "□", "□", "□", "■", "■", "■", "■", "■", "□", "■", "□", "■", "■", "■", "■"],
        ["□", "■", "■", "□", "□", "□", "■", "■", "□", "□", "□", "□", "□", "■", "■", "■"],
        ["□", "■", "■", "□", "■", "□", "□", "■", "□", "■", "□", "■", "□", "□", "□", "□"],
        ["□", "■", "■", "□", "■", "■", "□", "□", "□", "■", "□", "■", "□", "■", "■", "□"],
        ["□", "■", "■", "□", "□", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□", "□"],
        ["□", "□", "□", "□", "■", "□", "□", "□", "□", "■", "□", "■", "□", "■", "■", "■"],
        ["□", "■", "■", "□", "■", "□", "■", "■", "□", "□", "□", "□", "□", "□", "□", "□"],
        ["□", "□", "□", "□", "■", "□", "□", "■", "■", "■", "■", "■", "■", "■", "■", "★"]]

map2 = [["●", "□", "■", "■", "■", "■", "□", "□", "□", "■", "□", "□", "□", "□", "□", "■"],
        ["□", "□", "□", "■", "□", "□", "□", "■", "□", "■", "□", "■", "■", "■", "□", "■"],
        ["■", "■", "□", "■", "□", "■", "■", "■", "□", "□", "□", "■", "□", "■", "□", "■"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "■", "□", "■", "□", "□", "□", "■"],
        ["□", "□", "□", "□", "□", "■", "□", "■", "■", "■", "□", "■", "■", "■", "■", "■"],
        ["□", "■", "■", "■", "□", "■", "□", "□", "□", "□", "□", "□", "□", "□", "■", "□"],
        ["■", "■", "□", "□", "□", "■", "■", "□", "■", "■", "■", "■", "■", "□", "■", "□"],
        ["■", "□", "□", "■", "■", "■", "□", "□", "□", "■", "□", "□", "■", "■", "■", "□"],
        ["■", "□", "■", "■", "□", "□", "□", "■", "□", "□", "□", "■", "■", "□", "□", "□"],
        ["■", "□", "□", "■", "□", "■", "□", "■", "■", "■", "□", "■", "□", "□", "■", "■"],
        ["■", "■", "□", "■", "■", "■", "□", "■", "□", "□", "□", "□", "□", "■", "■", "□"],
        ["□", "□", "□", "■", "□", "□", "□", "□", "□", "□", "■", "□", "■", "□", "□", "□"],
        ["□", "■", "□", "□", "□", "■", "■", "□", "■", "■", "■", "□", "□", "□", "■", "□"],
        ["□", "■", "■", "■", "□", "■", "■", "□", "□", "□", "■", "□", "■", "■", "■", "■"],
        ["□", "□", "□", "■", "□", "■", "□", "□", "■", "□", "□", "□", "□", "□", "□", "□"],
        ["■", "■", "□", "■", "■", "■", "□", "■", "■", "□", "■", "■", "■", "■", "■", "□"],
        ["□", "□", "□", "□", "■", "□", "□", "■", "■", "□", "■", "□", "□", "□", "■", "■"],
        ["□", "■", "■", "□", "□", "□", "□", "■", "■", "□", "□", "□", "■", "□", "□", "★"]]

map3 = [["●", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
        ["□", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "□"],
        ["□", "■", "□", "□", "□", "■", "□", "■", "□", "□", "■", "□", "□", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "□", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "□", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "□", "■", "□", "□", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "□", "□", "■", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "□", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "□", "□", "■", "□", "■", "□", "□", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■", "■", "□", "■", "□", "■", "■", "■", "■"],
        ["□", "■", "□", "■", "□", "□", "□", "■", "□", "□", "■", "□", "■", "□", "□", "□"],
        ["□", "■", "□", "■", "■", "■", "■", "■", "□", "■", "■", "■", "■", "□", "■", "□"],
        ["□", "□", "□", "■", "■", "■", "■", "■", "□", "□", "□", "□", "□", "□", "■", "★"]]

map4 = [["●", "□", "■", "□", "□", "□", "□", "■", "■", "■", "■", "■", "□", "□", "□", "■"],
        ["■", "□", "■", "□", "■", "■", "□", "□", "■", "□", "□", "■", "□", "■", "□", "□"],
        ["□", "□", "■", "□", "□", "■", "■", "□", "□", "□", "□", "■", "□", "■", "■", "□"],
        ["□", "■", "■", "□", "□", "□", "■", "■", "□", "■", "□", "□", "□", "■", "□", "■"],
        ["□", "□", "□", "□", "■", "□", "□", "□", "■", "□", "■", "□", "■", "□", "□", "□"],
        ["■", "■", "■", "□", "■", "□", "■", "□", "□", "□", "□", "□", "□", "■", "■", "□"],
        ["□", "□", "□", "□", "■", "□", "□", "□", "■", "□", "■", "■", "□", "□", "□", "□"],
        ["□", "■", "□", "■", "■", "□", "■", "■", "□", "□", "■", "□", "□", "■", "■", "■"],
        ["□", "■", "□", "□", "■", "□", "■", "□", "□", "■", "□", "□", "■", "□", "□", "□"],
        ["□", "□", "■", "□", "■", "□", "■", "■", "■", "□", "□", "■", "□", "□", "■", "□"],
        ["□", "□", "□", "□", "□", "□", "■", "□", "□", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "■", "■", "□", "□", "■", "■", "□", "□", "□", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "□", "□", "■", "□", "□", "□", "■", "□", "□", "■", "□"],
        ["□", "■", "□", "□", "□", "■", "■", "□", "□", "■", "□", "■", "■", "□", "■", "□"],
        ["□", "□", "■", "■", "■", "□", "□", "□", "■", "■", "□", "■", "□", "□", "■", "□"],
        ["□", "□", "□", "■", "□", "□", "■", "■", "■", "■", "□", "□", "■", "■", "■", "□"],
        ["□", "■", "■", "□", "□", "□", "■", "■", "□", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "□", "□", "□", "■", "□", "□", "□", "□", "■", "□", "□", "□", "□", "■", "★"]]

map5 = [["●", "□", "□", "■", "□", "■", "■", "□", "□", "□", "■", "■", "□", "□", "□", "■"],
        ["□", "■", "□", "□", "□", "■", "□", "□", "■", "□", "□", "■", "□", "■", "□", "■"],
        ["□", "□", "□", "■", "□", "■", "□", "■", "■", "■", "□", "□", "□", "■", "□", "■"],
        ["□", "■", "■", "□", "□", "■", "□", "■", "■", "□", "■", "■", "■", "□", "□", "□"],
        ["□", "□", "□", "□", "■", "□", "□", "□", "□", "□", "■", "□", "■", "□", "■", "□"],
        ["■", "□", "■", "□", "□", "□", "■", "□", "■", "■", "□", "□", "□", "□", "■", "□"],
        ["□", "□", "■", "■", "□", "■", "□", "□", "□", "□", "□", "■", "■", "□", "□", "□"],
        ["□", "■", "□", "□", "□", "□", "□", "■", "□", "■", "□", "□", "□", "□", "■", "■"],
        ["□", "□", "□", "■", "■", "□", "■", "□", "□", "□", "■", "□", "□", "■", "□", "■"],
        ["□", "■", "□", "□", "□", "□", "■", "■", "□", "□", "□", "■", "■", "□", "□", "□"],
        ["■", "■", "□", "■", "□", "■", "□", "□", "■", "■", "□", "□", "□", "□", "■", "■"],
        ["□", "□", "□", "□", "□", "■", "□", "■", "□", "■", "□", "■", "□", "■", "■", "□"],
        ["□", "■", "■", "■", "□", "□", "□", "□", "□", "□", "□", "□", "□", "■", "■", "□"],
        ["□", "□", "□", "□", "□", "□", "■", "■", "■", "□", "■", "■", "□", "□", "□", "□"],
        ["□", "■", "□", "□", "□", "■", "□", "□", "□", "□", "□", "□", "■", "■", "□", "■"],
        ["□", "□", "■", "□", "■", "■", "□", "■", "□", "■", "□", "■", "■", "■", "□", "□"],
        ["■", "□", "□", "■", "□", "□", "□", "■", "□", "□", "■", "□", "□", "□", "■", "□"],
        ["■", "■", "□", "□", "□", "■", "□", "□", "■", "□", "□", "□", "■", "□", "□", "★"]]

map6 = [["●", "□", "■", "□", "■", "□", "□", "□", "□", "□", "□", "■", "□", "■", "□", "□"],
        ["■", "□", "□", "□", "□", "□", "■", "■", "■", "□", "■", "□", "□", "□", "□", "□"],
        ["□", "□", "■", "□", "■", "□", "□", "□", "□", "■", "■", "□", "■", "■", "■", "□"],
        ["□", "■", "□", "□", "□", "■", "■", "■", "□", "□", "■", "□", "□", "■", "□", "□"],
        ["□", "□", "□", "■", "□", "□", "□", "□", "■", "□", "□", "■", "□", "■", "□", "■"],
        ["■", "□", "■", "□", "□", "■", "■", "□", "□", "□", "■", "□", "□", "□", "□", "□"],
        ["□", "□", "□", "□", "■", "□", "□", "□", "□", "■", "□", "□", "■", "□", "■", "□"],
        ["■", "■", "□", "□", "□", "□", "■", "□", "■", "■", "□", "■", "■", "■", "□", "□"],
        ["■", "□", "□", "■", "■", "□", "□", "■", "□", "□", "□", "■", "■", "□", "□", "■"],
        ["□", "□", "■", "□", "□", "□", "■", "□", "□", "■", "■", "□", "□", "□", "■", "■"],
        ["□", "■", "□", "□", "■", "□", "■", "□", "■", "□", "■", "□", "■", "□", "□", "□"],
        ["□", "□", "□", "■", "■", "□", "□", "□", "■", "□", "■", "□", "□", "■", "□", "□"],
        ["■", "□", "□", "■", "■", "□", "■", "■", "□", "□", "■", "■", "□", "■", "■", "□"],
        ["□", "□", "□", "□", "□", "□", "■", "□", "□", "■", "■", "□", "□", "■", "□", "□"],
        ["□", "■", "■", "□", "■", "■", "□", "□", "■", "■", "■", "□", "■", "■", "□", "■"],
        ["□", "■", "□", "□", "■", "□", "□", "■", "■", "■", "■", "□", "□", "□", "■", "■"],
        ["□", "□", "■", "■", "□", "□", "■", "■", "□", "■", "□", "■", "■", "□", "□", "□"],
        ["■", "□", "□", "□", "□", "■", "□", "□", "□", "□", "□", "□", "□", "■", "■", "★"]]

#전역변수의 초기 값 설정
map_list = {1 : "map_1", 2 : "map_2", 3 : "map_3", 4 : "map_4", 5 : "map_5", 6 : "map_6"}
map_number = int(0)
map
output = ""
x = int(0)
y = int(0)
startTime = int(0)
endTime = int(0)
gameStart = False
key = 0


#map_list에 map을 담아서 random함수로 호출 -> map에 값을 넘겨줌
def start_game() :
        global map_list, map_number, map
        global output, gameStart, x,y, startTime
        startTime = time.time()
        map_number = randint(1,6)
        x = int(0)
        y = int(0)
        gameStart = True
        if(map_list.get(map_number)=="map_1") :
                map = map1    
        elif(map_list.get(map_number)=="map_2") :
                map = map2
        elif(map_list.get(map_number)=="map_3") :
                map = map3
        elif(map_list.get(map_number)=="map_4") :
                map = map4
        elif(map_list.get(map_number)=="map_5") :
                map = map5
        else : 
                map = map6
        
        for i in range(len(map)) :
                for j in range(len(map[0])) :
                        output = output + str(map[i][j]) + " "   
                if(i==len(map)-1): continue
                output += "\n"
        label_display.config(text=output)
        label_subtitle.config(text=map_list.get(map_number))

#수정된 문자열을 받아와 Display에 출력 -> 이동과정을 표현해줌
def update_map() :
        global map, map_list
        move = ""
        for i in range(len(map)) :
                for j in range(len(map[0])) :
                        move = move + str(map[i][j]) + " "   
                if(i==len(map)-1): continue
                move += "\n"
        label_display.config(text=move)

#게임을 완료했을때 실행 -> 텍스트 수정 후 메시지박스 출력
def escape_map() :
        global map, startTime, endTime, gameStart
        endTime = time.time()
        finish = ""
        for i in range(len(map)) :
                for j in range(len(map[0])) :
                        finish = finish + str(map[i][j]) + " "   
                if(i==len(map)-1): continue
                finish += "\n"
        label_display.config(text=finish)
        sec = (endTime-startTime)
        crtTime = datetime.timedelta(seconds = sec)
        crtTime_list = str(crtTime).split(".")
        gameStart=False
        mb.showinfo(title="<Escape>", message=crtTime_list[0]+"\n"+"탈출했습니다!!")

#위쪽 버튼 클릭시 실행 : y값 1 감소, 리스트의 텍스트 수정 -> 캐릭터가 이동하는 효과
#★을 만난다면 escape_map 실행
def move_up() :
        global map,x,y,gameStart
        if(gameStart):
                if(y>0) :
                        if(map[y-1][x]=="□") :
                                map[y][x] = "□"
                                y-=1
                                map[y][x] = "●"
                                update_map()
                        
                        elif(map[y-1][x]=="★") :
                                map[y][x] = "□"
                                y-=1
                                map[y][x] = "●"
                                escape_map()
                        
#아래쪽 버튼 클릭시 실행 : y값 1 증가, 리스트의 텍스트 수정 -> 캐릭터가 이동하는 효과
#★을 만난다면 escape_map 실행
def move_down() :
        global map,x,y,gameStart
        if(gameStart):
                if(y<17) :
                        if(map[y+1][x]=="□") :
                                map[y][x] = "□"
                                y+=1
                                map[y][x] = "●"
                                update_map()
                        
                        elif(map[y+1][x]=="★") :
                                map[y][x] = "□"
                                y+=1
                                map[y][x] = "●"
                                escape_map()
                        
#왼쪽 버튼 클릭시 실행 : x값 1 감소, 리스트의 텍스트 수정 -> 캐릭터가 이동하는 효과
#★을 만난다면 escape_map 실행              
def move_left() :
        global map,x,y,gameStart
        if(gameStart) :
                if(x>0) :
                        if(map[y][x-1]=="□") :
                                map[y][x] = "□"
                                x-=1
                                map[y][x] = "●"
                                update_map()
                        
                        elif(map[y][x-1]=="★") :
                                map[y][x] = "□"
                                x-=1
                                map[y][x] = "●"
                                escape_map()

#오른쪽 버튼 클릭시 실행 : x값 1 증가, 리스트의 텍스트 수정 -> 캐릭터가 이동하는 효과
#★을 만난다면 escape_map 실행       
def move_right() :
        global map,x,y,gameStart
        if(gameStart) :
                if(x<15) :
                        if(map[y][x+1]=="□") :
                                map[y][x] = "□"
                                x+=1
                                map[y][x] = "●"
                                update_map()
                        
                        elif(map[y][x+1]=="★") :
                                map[y][x] = "□"
                                x+=1
                                map[y][x] = "●"
                                escape_map()            

#게임 초기화
def reset_game() :
        global gameStart, output, map, endTime, startTime
        startTime = int(0)
        endTime = int(0)
        gameStart = False
        map[y][x] = "□"
        map[0][0] = "●"
        if(y==len(map)-1 and (x==len(map[0])-1)) :
                map[y][x] = "★"
        output = ""
        start_game()

def key_down(e) :
        global key
        key = e.keycode
        if(gameStart) :
                if(key==38) :
                        move_up()
                elif(key==40) :
                        move_down()
                elif(key==37) :
                        move_left()
                elif(key==39) :
                        move_right()

#게임 종료
def quit_game() :
        sys.exit()


maze = tk.Tk()
maze.title("Maze-Game")
maze.geometry('440x520')
maze.resizable(True,True)

label_subtitle_zone = tk.Label(master=maze)
label_subtitle_zone.pack()

label_subtitle_text = tk.Label(master=label_subtitle_zone, text='Escape Maze', font=('Arial',16))
label_subtitle_text.pack(side='top')

label_subtitle = tk.Label(master=label_subtitle_zone, text="", font=('Arial', 16))
label_subtitle.pack(side='top')

label_StateZone = tk.Label(master=maze)
label_StateZone.pack()

bt_reset = tk.Button(master=label_StateZone, text="다시하기", font=('Arial', 10), command=reset_game)
bt_reset.pack(side='left', padx=10)

bt_quit = tk.Button(master=label_StateZone, text="종료하기", font=('Arial', 10), command=quit_game)
bt_quit.pack(side='left')

bt_topArrow = tk.Button(master=maze, text="▲", font=('Arial',16), width=10, command=move_up)
bt_topArrow.pack()

label_center = tk.Label(master=maze)
label_center.pack()

bt_leftArrow = tk.Button(master=label_center, text="◀",font=('Arial',20), height=3, command=move_left)
bt_leftArrow.pack(side='left')

label_display = tk.Label(master=label_center, text=output, width=40, height=19)
label_display.pack(side='left')

bt_rightArrow = tk.Button(master=label_center, text="▶",font=('Arial',20), height=3, command=move_right)
bt_rightArrow.pack(side='right')

bt_bottomArrow = tk.Button(master=maze, text="▼", font=('Arial',16), width=10, command=move_down)
bt_bottomArrow.pack()



start_game()
maze.bind("<KeyPress>",key_down)
maze.mainloop()