from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
base = Tk()
base.geometry('300x150')

# Press the scroll button in the mouse then function will be called
def scroll(label):
   print('Scroll button clicked at x = % d, y = % d'%(label.x, label.y))
# Press the right button in the mouse then function will be called
def right_click(label):
   print('right button clicked at x = % d, y = % d'%(label.x, label.y))
# Press the left button twice in the mouse then function will be called
def left_click2(label):
   print('Double clicked left button at x = % d, y = % d'%(label.x, label.y))
def left_click(label):
    print('left mouse button clicked at x = % d, y = % d'%(label.x, label.y))


Function = Frame(base, height = 100, width = 200)
Function.bind('<Button-2>', scroll)
Function.bind('<Button-3>', right_click)
Function.bind('<Double 1>', left_click2)
Function.bind('<Button-1>',left_click)
Function.pack()
mainloop()