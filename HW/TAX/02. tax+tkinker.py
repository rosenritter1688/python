from tkinter import Tk,Label,Entry,Button
#import tkinter as tk
win = Tk()
win.title("測試tkinter")
win.geometry("600x600")                  #Width x Height
win.resizable(1,1)                       #1:True 0:False  此例 寬不可調, 高可調
#win.maxsize(width=1024, height=768)      #可調整最大尺寸
#win.minsize(width=100, height=100)       #可調整最小尺寸
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
myLabel1 = Label(win, text="sample A000000001/A/500000 ")
myLabel1.grid(row=0, column=0)

entry_data = Entry(win)
entry_data.grid(row=1,column=0,ipadx=141)
#--Label--
LabelShow = Label(win, text="",bg="grey")
#欠設定label的長度
LabelShow.grid(row=2, column=0)#ipadx=100  -> width   
#---BUTTON----


def calculate_tax():
    data = entry_data.get()
    #print(data)
    data_list=list()
    x = data.split("/")
    #print(x)
    data_list.append(x)
    #print(data_list)
    for id,city,income in data_list:
        #print(id,city,income)
        if float(income) >= 4530001:
            tax = (float(income) * 0.4) - 829600
        elif (float(income) >= 2420001) & (float(income) <= 4530000):
            tax = (float(income) * 0.3) - 376600
        elif (float(income) >= 1210001) & (float(income) <= 2420000):
            tax = (float(income) * 0.2) - 134600
        elif (float(income) >= 540001) & (float(income) <= 1210000):
            tax = (float(income) * 0.12) - 37800
        else:
            tax = (float(income) * 0.05)
        print("ID:身分證字號: " + id)
        print("城市: = " + city)
        print(f"收入: ${int(income):,}")
        print(f"所得稅: ${int(tax):,}")
        print("----------------------------------------------\n")
        #str_income = str(income) #!存檔用
        #str_tax =str(tax) #! 存檔用
        #! strip() 刪除左右兩邊的空白!!!有時候會有
        LabelShow.config(text=f"ID:身分證字號: {id.strip()} 城市: {city.strip()} 收入: {int(income):,} 所得稅: ${int(tax):,}")


        


ReadFile = Button(text='計算TAX',command=calculate_tax)
ReadFile.grid(row=0, column=2)
'''
取得label內容: lb.cget("text")
設定label內容:lb.config(text="設定內容文字")
'''

win.mainloop()  #主視窗一直循環被執行(常駐)   #一定要在最下面