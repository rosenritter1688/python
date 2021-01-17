from tkinter import Tk,Label,Entry,Button,END
import tkinter  ## for line 45 "tkinter.END"    as same as line 29 "END" but needed to import END at line 1
'''
摂氏 -> 華氏: oC × 1.8 + 32= oF
華氏 -> 摂氏: (oF - 32) ÷ 1.8 = oC
'''
#import tkinter as tk
win = Tk()
win.title("測試tkinter")
win.geometry("300x300") #Width x Height
win.resizable(0,1) #1:True 0:False  此例 寬不可調, 高可調
win.maxsize(width=1024, height=768) #可調整最大尺寸
win.minsize(width=100, height=100) #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico
win.config(bg="grey") #背景
win.attributes("-alpha",1) #透明度:0(全透)到1(不透)之間 
win.attributes("-topmost",True)  #出現在螢幕最上面
'''
BUTTON use place for location
myBtn = Button(win, text="C-->F")
myBtn.place(x=10, y=100) 
'''
#-------
def convertCtoF():
    #global f
    #global c
    c = float(myC.get())
    f = c*1.8+32
    myF.delete(0,END)     #clear all the content in ENTRY F   0 -> front END -> back    0,END -> means all
    myF.insert(0,str(f))  #0 是放前面 END是放後面  END要import END
#! function 一定要放在設定COMMAND的上面 

cToF = Button(text='C-->F',command=convertCtoF)
cToF.grid(row=0, column=0)
#--------
myLabel = Label(win, text="C")
myLabel.grid(row=0, column=1)
#-------
myC = Entry(win)
myC.grid(row=0,column=2)
#-------
def convertFtoC():
    f = float(myF.get())
    c = (f-32)/1.8
    myC.delete(0,tkinter.END)
    myC.insert(0,str(c)) #0 是放前面 END是放後面  END要import END


fToC = Button(text='F-->C',command=convertFtoC)
fToC.grid(row=1, column=0)
#--------
myLabel2 = Label(win, text="F")#Label放到win裡面 show F
myLabel2.grid(row=1, column=1)
#-------
myF = Entry(win)#entry 放到win裡面
myF.grid(row=1,column=2)



win.mainloop()  #主視窗一直循環被執行(常駐)   #一定要在最下面


