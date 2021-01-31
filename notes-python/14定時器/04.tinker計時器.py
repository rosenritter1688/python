'''
win.after(1000,go)#每1000毫秒後跑一次購
'''



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

def go():
    print('----')
    win.after(1000,go)#每1000毫秒後跑一次購
'''
    注意
    win.after(1000,go)
    跟loop也會一直跑print
'''


btn = Button(win,text='click me', command=go)
             #button放在視窗win裡面
             
btn.place(x=0,y=0)



win.mainloop()