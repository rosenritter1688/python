# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:25:13 2020

'''
for x in range (1,10):
    for n in range(1,10):
        print("{} x {} = {:2}".format(x,n,x*n))

'''
"""
from tkinter import *
win = Tk()
win.geometry('500x500')
win.config(bg='lightgreen')
def showOdd():
    outs = ''
    for idx in range(1, 101):
        if idx%2 != 0:
           outs += str(idx) + '\n'
           
    #label1.config(text=outs)
    text1.insert(1.0, outs) ###
btnOdd = Button(win, text='odd and even', command=showOdd)
btnOdd.grid(row=0, column=0)
btn1 = Button(win, text='odd', command=showOdd)
btn1.grid(row=0, column=1, sticky=W+E)



text1 = Text(win, width=20, height=20)
text1.grid(row=1, column=0, columnspan=2)

scroll1 = Scrollbar(win, command=text1.yview)
scroll1.grid(row=1, column=2, sticky=N+S)

def showValue(self):
    label1.config(text=int(scale1.get()))

scale1 = Scale(win,orient=HORIZONTAL,from_=0, to_=1000, command=showValue)
scale1.grid(row=3, column=0,columnspan=2,sticky=W+E)
label1 = Label(win, text='____')
label1.grid(row=3, column=2)

def showValue2(self):
    label2.config(text=int(scale2.get()))
scale2 = Scale(win,orient=HORIZONTAL,from_=0, to_=1000, command=showValue2)
scale2.grid(row=4, column=0,columnspan=2,sticky=W+E)

label2 = Label(win, text='____')
label2.grid(row=4, column=2)

win.mainloop()
