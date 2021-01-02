


from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

import numpy
from pandas import DataFrame
import matplotlib.pyplot as plt
win = Tk()
win.geometry('500x500')
win.title("統計圖表")
x=list(range(1,11))

y1 = list(numpy.sin(x))  # list1

y2 = list(numpy.cos(x))  #list2
print(x, y1, y2)
fig = Figure(figsize = (5, 5),  dpi = 100)  #1.設定Figure
plot1 = fig.add_subplot(111) #2.設定subplot(子圖)
plot1.plot(y1, 'b') #3.在子圖畫圖(plot)
plot1.plot(y2,'r')
canvas = FigureCanvasTkAgg(fig, master = win) #4.設定canvas並將Figure貼上
#canvas.draw() 
canvas.get_tk_widget().grid(row=2, column=0) #5.將canvas貼在window
win.mainloop()
