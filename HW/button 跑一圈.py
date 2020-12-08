'''
win.after(1000,go)#每1000毫秒(1 秒)後跑一次購
'''


import time
from tkinter import Tk,Button
win = Tk()
      ##Tk() 開一個視窗的意思並命名此視窗名稱為win
win.title("測試tkinter")
win.geometry("600x600")                  #Width x Height
win.resizable(0,1)                       #1:True 0:False  此例 寬不可調, 高可調
win.maxsize(width=1024, height=768)      #可調整最大尺寸
win.minsize(width=100, height=100)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico
win.config(bg="grey")                    #背景
win.attributes("-alpha",1)               #透明度:0(全透)到1(不透)之間 
win.attributes("-topmost",True)          #出現在螢幕最上面


x_position = 0
y_position = 0


def go():
    global x_position,y_position
    if (x_position < 500) & (y_position == 0):
        #time.sleep(0.5)
        x_position += 10
        #print(str(x_position))
        btn.place(x=x_position,y=0)
        win.after(10,go)#每100毫秒後跑一次購
    else:
        go_down()
def go_down():
    global x_position,y_position
    if (x_position == 500) & (y_position < 500):
        #time.sleep(0.5)
        y_position += 10
        #print(str(x_position))
        btn.place(x=500,y=y_position)
        win.after(10,go)#每100毫秒後跑一次購
    else:
        go_left()
def go_left():
    global x_position,y_position
    if x_position > 0:
        #time.sleep(0.5)
        x_position -= 10
        #print(str(x_position))
        btn.place(x=x_position,y=500)
        win.after(10,go)#每100毫秒後跑一次購
    else:
        go_up()
def go_up():
    global x_position,y_position
    if y_position > 0:
        #time.sleep(0.5)
        y_position -= 10
        #print(str(x_position))
        btn.place(x=0,y=y_position)
        win.after(10,go)#每100毫秒後跑一次購
    #else:
        


btn = Button(win,text='click me', command=go)
             #button放在視窗win裡面
btn.place(x=0,y=0)
win.mainloop()