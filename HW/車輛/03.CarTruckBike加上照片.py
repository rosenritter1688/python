'''
某交通路口交通工具到達狀況:
卡車:5秒鐘到達1台,  10秒離開1台
汽車:3秒鐘到達1台,   5秒離開1台
摩托車:1秒鐘到達1台, 2秒離開1台 
試用計時器, 顯示每秒交通路口的工具數量, 直到60秒為止 
'''
from tkinter import *
import time
from threading import Timer  ##!!!!
#import tkinter as tk
win = Tk()                               #開一個視窗並命名此視窗為win
win.title("車流量")
win.geometry("1000x900")                 #Width x Height
#win.resizable(0,1)                       #1:True 0:False  此例 寬不可調, 高可調
#win.maxsize(width=1024, height=768)      #可調整最大尺寸
#win.minsize(width=100, height=100)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico
#win.config(bg="grey")                    #背景
#win.attributes("-alpha",1)               #透明度:0(全透)到1(不透)之間 
#win.attributes("-topmost",True)          #出現在螢幕最上面
count_down = 0
bike = 0
car = 0
truck = 0
x = 0
pos_x = 0           #x position for bike
pos_x_car = 0       #x position for car 
pos_x_truck = 0     #x position for truck
def start_countdown():
    global count_down
    global bike
    global car
    global truck
    global x
    global pos_x
    global pos_x_car
    global pos_x_truck
    for x in range(60):
        time.sleep(1)
        count_down += 1
        myLabel_count_down.config(text="") ##刪除之前殘留在label的資料用
        myLabel_count_down.config(text="{}".format(count_down))
        print(str(count_down) + " seconds\n")
        if (count_down % 5 == 0) & (count_down % 3 == 0) & (count_down % 1 == 0):
            truck += 1
            car += 1
            bike += 1
            print("total bike +1 = {}".format(str(bike)))
            myLabel_bike2.config(text="")                                   ##刪除之前殘留在label的資料用
            myLabel_bike2.config(text="{}".format(bike))
            pos_x += 10
            Label_bike = Label(win,text='bike_image',image=bike_img)         
            '''
            Label_bike = Label(win,text='bike_image',image=bike_img)
            這個沒打的話一直只有一個LABEL在上面
            '''
            Label_bike.place(x=pos_x,y=500)
            Tk.update(win)                                                  #refresh win named win 
            print("total car +1 = {}".format(str(car)))
            myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_car2.config(text="{}".format(car))
            pos_x_car += 10
            Label_car = Label(win,text='car_image',image=car_img)
            Label_car.place(x=pos_x_car,y=600)
            Tk.update(win)
            print("total truck +1 = {}\n".format(str(truck)))
            myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_truck2.config(text="{}".format(truck))
            pos_x_truck += 60
            Label_truck = Label(win,text='truck_image',image=truck_img)
            Label_truck.place(x=pos_x_car,y=700)
            Tk.update(win)
        elif (count_down % 5 == 0) & (count_down % 3 == 0):
            truck += 1
            car += 1
            print("total car +1 = {}".format(str(car)))
            myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_car2.config(text="{}".format(car))
            pos_x_car += 10.
            Label_car = Label(win,text='car_image',image=car_img)
            Label_car.place(x=pos_x_car,y=600)
            Tk.update(win)
            print("total truck +1 = {}\n".format(str(truck)))
            myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_truck2.config(text="{}".format(truck))
            pos_x_truck += 60
            Label_truck = Label(win,text='truck_image',image=truck_img)
            Label_truck.place(x=pos_x_car,y=700)
            Tk.update(win)
        elif (count_down % 5 == 0) & (count_down % 1 == 0):
            truck += 1
            bike += 1
            print("total bike +1 = {}".format(str(bike)))
            myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_bike2.config(text="{}".format(bike))
            pos_x += 10
            Label_bike = Label(win,text='bike_image',image=bike_img)
            Label_bike.place(x=pos_x,y=500)
            Tk.update(win)
            print("total truck +1 = {}\n".format(str(truck)))
            myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_truck2.config(text="{}".format(truck))
            pos_x_truck += 60
            Label_truck = Label(win,text='truck_image',image=truck_img)
            Label_truck.place(x=pos_x_car,y=700)
            Tk.update(win)
        elif (count_down % 3 == 0) & (count_down % 1 == 0):
            car += 1
            bike += 1
            print("total bike +1 = {}".format(str(bike)))
            myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_bike2.config(text="{}".format(bike))
            pos_x += 10
            Label_bike = Label(win,text='bike_image',image=bike_img)
            Label_bike.place(x=pos_x,y=500)
            Tk.update(win)
            print("total car +1 = {}\n".format(str(car)))
            myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_car2.config(text="{}".format(car))
            pos_x_car += 10
            Label_car = Label(win,text='car_image',image=car_img)
            Label_car.place(x=pos_x_car,y=600)
            Tk.update(win)
        elif count_down % 5 == 0:
            truck += 1
            print("total truck +1 = {}\n".format(str(truck)))
            myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_truck2.config(text="{}".format(truck))
            pos_x_truck += 60
            Label_truck = Label(win,text='truck_image',image=truck_img)
            Label_truck.place(x=pos_x_car,y=700)
            Tk.update(win)
        elif count_down % 3 == 0:
            car += 1
            print("total car +1 = {}\n".format(str(car)))
            myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_car2.config(text="{}".format(car))
            pos_x_car += 10
            Label_car = Label(win,text='car_image',image=car_img)
            Label_car.place(x=pos_x_car,y=600)
            Tk.update(win)
        elif count_down % 1 == 0:
            bike += 1
            print("total bike +1 = {}\n".format(str(bike)))
            myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
            myLabel_bike2.config(text="{}".format(bike)) 
            pos_x += 10
            Label_bike = Label(win,text='bike_image',image=bike_img)
            Label_bike.place(x=pos_x,y=500)
            Tk.update(win)
    print("----------------------------------")
    print("total = {} seconds".format(str(count_down)))
    print("total bikes = {}".format(str(bike)))
    print("total cars = {}".format(str(car)))
    print("total truck = {}".format(str(truck)))

            

#Button - start
start_btn = Button(text='start', bg='green', command=start_countdown)
start_btn.grid(row=0, column=0)
#Label-traffic light img
TrafficLights_img = PhotoImage(file='C:\\Users\Bruce Ashbee\\Documents\\traffic-lights-red.PNG')
TrafficLights_label = Label(win, text="traffic_light", bg="green",image=TrafficLights_img)
TrafficLights_label.grid(row = 1, column=0)
#------------------------------------FOR showing numbers--------------------------------------------
#Label- bike number
myLabel_bike = Label(win, text="Bike : ")
myLabel_bike.grid(row=3, column=0,sticky="w")
myLabel_bike.grid(row=3, column=0,sticky="w")
myLabel_bike2 = Label(win, text="")
myLabel_bike2.grid(row=3, column=1,sticky="e")
#Label- car number
myLabel_car = Label(win, text="Car : ")
myLabel_car.grid(row=4, column=0,sticky="w")
myLabel_car2 = Label(win, text="")
myLabel_car2.grid(row=4, column=1,sticky="e")
#Label - truck number
myLabel_truck = Label(win, text="Truck : ")
myLabel_truck.grid(row=5, column=0,sticky="w")
myLabel_truck2 = Label(win, text="")
myLabel_truck2.grid(row=5, column=1,sticky="e")
#Label - count_down
myLabel_count_down = Label(win, text="count_down(sec) : ")
myLabel_count_down.grid(row=6, column=0,sticky="w")
myLabel_count_down = Label(win, text="")
myLabel_count_down.grid(row=6, column=1,sticky="e")
#------------------------------For labels with imnages
#Label bike
#Label_bike = Label(win, text="bike_img")  ~~>每次LOOP裡面都有打了
car_img = PhotoImage(file='C:\\Users\\Bruce Ashbee\\Documents\\葉老師PYTHON\\交通工具\\car.PNG')
#Label_bike.config(image=car_img)  ~~~~~>每次LOOP裡面都有打了
bike_img = PhotoImage(file='C:\\Users\\Bruce Ashbee\\Documents\\葉老師PYTHON\\交通工具\\motor.PNG')
truck_img = PhotoImage(file='C:\\Users\\Bruce Ashbee\\Documents\\葉老師PYTHON\\交通工具\\trank.PNG')









win.mainloop()  #主視窗一直循環被執行(常駐)   #一定要在最下面