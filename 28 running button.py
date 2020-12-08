from threading import Timer
import time
from tkinter import Tk,Button



win=Tk()
win.geometry("800x300")

position= 1 
dif = 10

def go():
    global position, dif
    myBtn.place(x=position, y=0)
    position = position + dif
    #print(position, dif)
    if position > 500:
        position = 0
    win.after(10,go)
myBtn = Button(text='Time', bg='green', command=go) #bg doesnt work on MAC, MAC may use highlightbackground='#3E4149'
myBtn.place(x=1,y=1)
win.mainloop()



