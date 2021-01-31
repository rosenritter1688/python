'''
win.after(1000,go)#每1000毫秒後跑一次購
'''


import time
from tkinter import *
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

#WHILE LOOP BUTTON只會跑到終點但是部會一個一個跑--?已經解決!!!
#加上 Tk.update(win) 就可以了
def go():
    global x_position
 
    while x_position <= 500:
        time.sleep(0.1)
        x_position += 10
        print(str(x_position))
        btn.place(x=x_position,y=0)
        Tk.update(win)#refresh window called win        
        '''要用refresh不然會看不到BUTTON再跑'''
        #win.after(1000,go)#每1000毫秒後跑一次購          
        '''while loop用win.after沒用依舊會跑很快'''
        

    
def go2():
    global x_position
 
    if x_position <= 500:
        #time.sleep(0.5)
        x_position += 10
        print(str(x_position))
        btn2.place(x=x_position,y=100)
        #Tk.update(win)#refresh win                 
        '''跟while loop不一樣不需要用refresh window就可以看到button再跑'''
        win.after(1000,go2)#每1000毫秒後跑一次GO      

btn = Button(win,text='click me', command=go)
             #button放在視窗win裡面
             
btn.place(x=0,y=0)

btn2 = Button(win,text='def go2', command=go2)
             #button放在視窗win裡面
             
btn2.place(x=0,y=100)



win.mainloop()
#myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
#            myLabel_car2.config(text="{}".format(car))
#            Tk.update(win)