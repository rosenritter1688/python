#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:00:12 2020

 

@author: yinchen
"""
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as msg
from PIL import ImageTk, Image

 

def gen(vehicle, name):
    for i in range(vehicle):
        x = i * 65 + 35
        if (name == 'Truck'):
            body_canvas.create_image(x, 100, image=pathTruck)            
        elif (name == 'Car'):
            body_canvas.create_image(x, 200, image=pathCar)
        else:
            if i >= 15:
                x = (i-15) * 65 + 35
                body_canvas.create_image(x, 400, image=pathMoto)
            else:
                body_canvas.create_image(x, 300, image=pathMoto)
def enter():
    global timer, truck, car, moto
    body_canvas.delete('all')
    timer += 1
    moto += 1
    if (timer % 2 == 0):
        moto -= 1
    if (timer % 3 == 0):
        car += 1
    if (timer % 5 == 0):
        truck += 1
        car -= 1 
    if (timer % 10 == 0):
        truck -= 1

 

    show.config(text=f'{timer}秒 {truck}台卡車 {car}台汽車 {moto}台機車')
    gen(truck, 'Truck')
    gen(car, 'Car')
    gen(moto, 'Moto') 

 

    if (timer == 60):
        msg.showinfo(title='總結', message=f'一分鐘內總共有{truck}台卡車,{car}台汽車,{moto}台機車')
        return print(f'一分鐘內總共有{truck}台卡車,{car}台汽車,{moto}台機車')
    
    win.after(100, enter)
        
win = tk.Tk()
win.title('Timer')
win.geometry('1000x600')
win.config(bg='#E0FFFF')

 

head_canvas = tk.Canvas(win, bg='#E0FFFF', width=1000, height=120)
head_canvas.config(highlightthickness=0)
head_canvas.pack(side='top')

 

body_canvas = tk.Canvas(win, bg='#E0FFFF', width=1000, height=480)
body_canvas.config(highlightthickness=0)
body_canvas.pack(side='bottom')

 

truck = car = moto = 0
timer = 0

 

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
show = tk.Label(head_canvas,text='0秒 0台卡車 0台汽車 0台機車', bg='#E0FFFF', font=fontStyle)
show.pack()
head_canvas.create_window(500, 50, window=show)

 


# open and resize image
pathTraffic = Image.open('traffic-lights-green.PNG').resize((100,100), Image. ANTIALIAS)
pathTraffic = ImageTk.PhotoImage(pathTraffic)
imgTraffic = tk.Button(win, image=pathTraffic, bg='#E0FFFF', bd=0, command=enter)
head_canvas.create_window(50, 50, window=imgTraffic)

 


pathTruck = Image.open('trank.png').resize((60,60), Image. ANTIALIAS)
pathTruck = ImageTk.PhotoImage(pathTruck)

 

pathCar = Image.open('car.png').resize((60,60), Image. ANTIALIAS)
pathCar = ImageTk.PhotoImage(pathCar)

 

pathMoto = Image.open('motor.png').resize((60,60), Image. ANTIALIAS)
pathMoto = ImageTk.PhotoImage(pathMoto)

 

win.mainloop()