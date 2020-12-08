

from tkinter import Tk,Scale,SCROLL,Text,Scrollbar,END
import tkinter as tk
win=Tk()
win.geometry("800x500")
win.config(bg='lightblue')
#-------------------------

def calculate(self):
    result.delete('1.0', END)                   #! need to import END  
    value_1 = int(scale.get())
    #s = value_1 + 1
    for i in range (1,value_1 + 1):
        if i % 2 != 0:
            print(i)
            result.insert(END, f"{i:5} \n")    #! need to import END
            #result.insert(1.0, f"{i:5} \n")   #! 1.0 從上面開始寫，就會最新的在上面 
scale = Scale(win, from_ = 1, to_ = 100,showvalue=1,command=calculate)
scale.grid(row=0, column=0, sticky = "NS")
#----------------------
result = Text(win)
result.grid(row=0, column=1)
#-----------------------
scroll = Scrollbar(win)
scroll.grid(row=0, column=2, sticky = "NS")
#------------------------
###testing
win.mainloop()
