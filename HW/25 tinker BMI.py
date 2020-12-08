from tkinter import Tk,Button,Label,Entry
'''
摂氏 -> 華氏: oC × 1.8 + 32= oF
華氏 -> 摂氏: (oF - 32) ÷ 1.8 = oC
'''
#import tkinter as tk
win = Tk()
win.title("測試tkinter")
win.geometry("300x300")                  #Width x Height
win.resizable(0,1)                       #1:True 0:False  此例 寬不可調, 高可調
win.maxsize(width=1024, height=768)      #可調整最大尺寸
win.minsize(width=100, height=100)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico
win.config(bg="grey")                    #背景
win.attributes("-alpha",1)               #透明度:0(全透)到1(不透)之間 
win.attributes("-topmost",True)          #出現在螢幕最上面
'''
BUTTON use place for location
myBtn = Button(win, text="C-->F")
myBtn.place(x=10, y=100) 
'''
#---LABEL-----
myLabel1 = Label(win, text="Weigth(kg) : ")
myLabel1.grid(row=0, column=0)
myLabel2 = Label(win, text="Heigth(cm) : ")
myLabel2.grid(row=1, column=0)
myLabel3 = Label(win, text="BMI : ")
myLabel3.grid(row=2, column=0)
#-----ENTRY--
KGentry = Entry(win)
KGentry.grid(row=0,column=1)
Hentry = Entry(win)
Hentry.grid(row=1,column=1)
#--Label--
myLabel4 = Label(win, text="")
#欠設定label的長度
myLabel4.grid(row=2, column=1,sticky="e")#sticky是要靠的方向  e = 東方
#---BUTTON----
def calculateBMI():
    kg = float(KGentry.get())
    height = float(Hentry.get())
    height2 = height/100
    bmi = float(kg)/((float(height2)*float(height2)))
    myLabel4.config(text="") ##刪除之前殘留在label的資料用
    myLabel4.config(text="{:.2f}".format(bmi))


bmi = Button(text='get BMI',command=calculateBMI)
bmi.grid(row=2, column=2)
'''
取得label內容: lb.cget("text")
設定label內容:lb.config(text="設定內容文字")

'''



win.mainloop()  #主視窗一直循環被執行(常駐)   #一定要在最下面


