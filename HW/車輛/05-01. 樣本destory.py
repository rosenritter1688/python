'''
會刪除但是只會從第一個刪除
'''
from tkinter import *
import time
win = Tk()
win.geometry('1000x560')

img_list = []#使用list從放所有產生的button以便後面可以依據刪除

def add_Image():
    for a in range(5):
        btn = Button(win,text='image',image=car_img)
        btn.place(x=a*150, y=250)
        Tk.update(win)
        time.sleep(1)
        img_list.append(btn)
        print(img_list)
        '''
        button 資訊放到 img_list後的樣子
        '''
        #[<tkinter.Button object .!button3>]
        #[<tkinter.Button object .!button3>, <tkinter.Button object .!button4>]
        #[<tkinter.Button object .!button3>, <tkinter.Button object .!button4>, <tkinter.Button object .!button5>]
        #[<tkinter.Button object .!button3>, <tkinter.Button object .!button4>, <tkinter.Button object .!button5>, <tkinter.Button object .!button6>]
        #[<tkinter.Button object .!button3>, <tkinter.Button object .!button4>, <tkinter.Button object .!button5>, <tkinter.Button object .!button6>, <tkinter.Button object .!button7>]
def del_Image():
    for num, content in enumerate(img_list,start=1): #給img_list裡面的資料編號
                       #see list or tuple notes of enumberate
                       #                    從幾號開始編號
        print(num,content)
        content.destroy()
        '''
        刪除順序
        1 .!button3
        2 .!button4
        3 .!button5
        4 .!button6
        5 .!button7

        '''
        Tk.update(win)
        time.sleep(1)
        
             
    pass
#    for a,b in enumerate(img_list,0)

addbtn = Button(win, text='add btn', command=add_Image)
addbtn.place(x=0, y=0)
car_img = PhotoImage(file='C:\\Users\\Bruce Ashbee\\Documents\\葉老師PYTHON\\交通工具\\car.PNG')

del_btn = Button(win, text='del btn', command=del_Image)
del_btn.place(x=0, y=100)
win.mainloop()