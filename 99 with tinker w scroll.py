# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:25:13 2020

"""
from tkinter import *
win = Tk()
win.geometry('500x500')
win.config(bg='lightgreen')
def show_multiplication_tables():
    value_1 = int(scale1.get())
    value_2 = int(scale2.get())
    for x in range (1,value_1+1):
        for n in range(1,value_2+1):
            print("{:4} x {:4} = {:6}".format(x,n,x*n))
            text1.insert(END, f"{x:4} x {n:4} = {x*n:6}\n")
            Tk.update(win)
                         #! 注意 不打END的話打1.0會塞在最前面
                         #! 也就是顯示資料都是從新的排到舊的
btnOdd = Button(win, text='乘法表', command=show_multiplication_tables)
btnOdd.grid(row=0, column=0)

text1 = Text(win, width=20, height=20)
text1.grid(row=1, column=0, columnspan=2)

scroll1 = Scrollbar(win, command=text1.yview)
scroll1.grid(row=1, column=2, sticky=N+S)

def showValue(self):
    label1.config(text=int(scale1.get()))

scale1 = Scale(win,orient=HORIZONTAL,from_=0, to_=100,label='x', command=showValue)
scale1.grid(row=3, column=0,columnspan=2,sticky=W+E)

label1 = Label(win, text='X')
label1.grid(row=3, column=2)

def showValue2(self):
    label2.config(text=int(scale2.get()))
scale2 = Scale(win,orient=HORIZONTAL,from_=0, to_=100,label='y', command=showValue2)
scale2.grid(row=4, column=0,columnspan=2,sticky=W+E)

label2 = Label(win, text='Y')
label2.grid(row=4, column=2)

win.mainloop()
