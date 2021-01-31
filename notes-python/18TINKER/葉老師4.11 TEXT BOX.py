'''
file_name = "H2"
actual_file_name = "\'C:\\Users\\Bruce Ashbee\\Documents\\葉老師PYTHON\\poker圖檔\\" + file_name.strip() + '.PNG\''

print(actual_file_name)


text1.insert(1, 0,out)
           #1,0 ->放的位置
#Tkinker TEXT
text1 = Text(win, width=20, height=20)
text1.grid(row=1,column=0)

scroll_1 = Scrollbar(win)
scroll_1.grid(row=1,)
'''



from tkinter import *
import time
from threading import Timer  ##!!!!
#import tkinter as tk
win = Tk()                               #開一個視窗並命名此視窗為win
win.title("車流量")
win.geometry("1000x500")                 #Width x Height
#win.resizable(0,1)                       #1:True 0:False  此例 寬不可調, 高可調
#win.maxsize(width=1024, height=768)      #可調整最大尺寸
#win.minsize(width=100, height=100)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico
#win.config(bg="grey")                    #背景
#win.attributes("-alpha",1)               #透明度:0(全透)到1(不透)之間 
#win.attributes("-topmost",True)          #出現在螢幕最上面

def show_odd_no ():
    output = ''
    for idx in range(1,101):
        if idx % 2 != 0:
            output += str(idx) + '\n'
    text1.insert(1.0, output)#寫到text BOX裡面去 #1.0寫到text最前面 1.0改成END是寫在最後面
btn = Button(win, text='odd and even',command = show_odd_no)
btn.grid(row=0,column=0)

label1 = Label(win, text='-----')
label1.grid(row=1,column=0)

text1 = Text(win, width=100,height=100)
text1.grid(row=1,column=1)

scroll1 = Scrollbar(win,command=text1.yview)
scroll1.grid(row=1,column=2,sticky=N+S)


scroll2 = Scrollbar(win,command=text1.yview)
scroll2.grid(row=2,column=2,sticky=W+E)



win.mainloop()  #主視窗一直循環被執行(常駐)   #一定要在最下面