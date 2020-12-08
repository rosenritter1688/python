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
pos_x = -10           #x position for bike
pos_x_car = -30       #x position for car 
pos_x_truck = -60     #x position for truck

bike_list = []        #(bike list) for deleting
car_list = []         #(car list) for deleting
truck_list = []       #(truck list) for deleting
#flag = "go"
count_down_for_green = 0
def stop():
    print('stop')
    return
def change_green():
    TrafficLights_label.configure(image=TrafficLights_green_img)
    global count_down_for_green
    global flag
    global bike
    global car
    global truck
    global pos_x
    global pos_x_car
    global pos_x_truck
    global bike_list, car_list, truck_list
    #while flag != "stop":
    for x in range(61):
        time.sleep(1)
        count_down_for_green += 1
        myLabel_count_down.config(text="") ##刪除之前殘留在label的資料用
        myLabel_count_down.config(text="{}".format(count_down_for_green))
        Tk.update(win)
        print('\n')
        print(str(count_down_for_green) + " seconds\n")
        if count_down_for_green == 61:
            return stop()
        elif count_down_for_green <=60:
            if (count_down_for_green % 10 == 0) & (count_down_for_green % 5 == 0) & (count_down_for_green % 2 == 0):
                truck -= 1
                car -= 1
                bike -= 1
                print("total bike -1 = {}".format(str(bike)))
                myLabel_bike2.config(text="")                                   ##刪除之前殘留在label的資料用
                myLabel_bike2.config(text="{}".format(bike))
                bike_list.pop().destroy()
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)                                                  #refresh win named win 
                print("total car -1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                car_list.pop().destroy()
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
                print("total truck -1 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                truck_list.pop().destroy()
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif (count_down_for_green % 10 == 0) & (count_down_for_green % 5 == 0):
                truck -= 1
                car -= 1
                print("total car -1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                car_list.pop().destroy()
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
                print("total truck 11 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                truck_list.pop().destroy()
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif (count_down_for_green % 10 == 0) & (count_down_for_green % 2 == 0):
                truck -= 1
                bike -= 1
                print("total bike -1 = {}".format(str(bike)))
                myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_bike2.config(text="{}".format(bike))
                bike_list.pop().destroy()
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)
                print("total truck -1 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                truck_list.pop().destroy()
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif (count_down_for_green % 5 == 0) & (count_down_for_green % 2 == 0):
                car -= 1
                bike -= 1
                print("total bike -1 = {}".format(str(bike)))
                myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_bike2.config(text="{}".format(bike))
                bike_list.pop().destroy()
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)
                print("total car -1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                car_list.pop().destroy()
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
            elif count_down_for_green % 10 == 0:
                truck -= 1
                print("total truck -1 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                truck_list.pop().destroy()
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif count_down_for_green % 5 == 0:
                car -= 1
                print("total car -1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                car_list.pop().destroy()
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
            elif count_down_for_green % 2 == 0:
                bike -= 1
                print("total bike -1 = {}".format(str(bike)))
                myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_bike2.config(text="{}".format(bike)) 
                bike_list.pop().destroy()
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)



    
def change_yellow():
    TrafficLights_label.configure(image=TrafficLights_yellow_img)
    count_down_yellow = 0
    time.sleep(1)
    count_down_yellow += 1
    myLabel_count_down.config(text="") ##刪除之前殘留在label的資料用
    myLabel_count_down.config(text="{}".format(count_down_yellow))
    Tk.update(win)
    print("yellow light is changed and wait for 3 seconds")
    while count_down_yellow <= 4:
        if count_down_yellow == 4:
            change_green()
        else:
            count_down_yellow += 1
            myLabel_count_down.config(text="") ##刪除之前殘留在label的資料用
            myLabel_count_down.config(text="{}".format(count_down_yellow))
            Tk.update(win)

        

def start_countdown():
    global count_down
    global bike
    global car
    global truck
    #global x
    global pos_x
    global pos_x_car
    global pos_x_truck
    global bike_list, car_list, truck_list
    for x in range(61):
        time.sleep(1)
        count_down += 1
        myLabel_count_down.config(text="") ##刪除之前殘留在label的資料用
        myLabel_count_down.config(text="{}".format(count_down))
        print('\n')
        print(str(count_down) + " seconds\n")
        if count_down <= 60:
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
                Label_bike.place(x=pos_x,y=350)
                bike_list.append(Label_bike)
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)                                                  #refresh win named win 
                print("total car +1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                pos_x_car += 30
                Label_car = Label(win,text='car_image',image=car_img)
                Label_car.place(x=pos_x_car,y=550)
                car_list.append(Label_car)
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
                print("total truck +1 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                pos_x_truck += 60
                Label_truck = Label(win,text='truck_image',image=truck_img)
                Label_truck.place(x=pos_x_truck,y=700)
                truck_list.append(Label_truck)
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif (count_down % 5 == 0) & (count_down % 3 == 0):
                truck += 1
                car += 1
                print("total car +1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                pos_x_car += 30.
                Label_car = Label(win,text='car_image',image=car_img)
                Label_car.place(x=pos_x_car,y=550)
                car_list.append(Label_car)
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
                print("total truck +1 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                pos_x_truck += 60
                Label_truck = Label(win,text='truck_image',image=truck_img)
                Label_truck.place(x=pos_x_truck,y=700)
                truck_list.append(Label_truck)
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif (count_down % 5 == 0) & (count_down % 1 == 0):
                truck += 1
                bike += 1
                print("total bike +1 = {}".format(str(bike)))
                myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_bike2.config(text="{}".format(bike))
                pos_x += 10
                Label_bike = Label(win,text='bike_image',image=bike_img)
                Label_bike.place(x=pos_x,y=350)
                bike_list.append(Label_bike)
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)
                print("total truck +1 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                pos_x_truck += 60
                Label_truck = Label(win,text='truck_image',image=truck_img)
                Label_truck.place(x=pos_x_truck,y=700)
                truck_list.append(Label_truck)
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif (count_down % 3 == 0) & (count_down % 1 == 0):
                car += 1
                bike += 1
                print("total bike +1 = {}".format(str(bike)))
                myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_bike2.config(text="{}".format(bike))
                pos_x += 10
                Label_bike = Label(win,text='bike_image',image=bike_img)
                Label_bike.place(x=pos_x,y=350)
                bike_list.append(Label_bike)
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)
                print("total car +1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                pos_x_car += 30
                Label_car = Label(win,text='car_image',image=car_img)
                Label_car.place(x=pos_x_car,y=550)
                car_list.append(Label_car)
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
            elif count_down % 5 == 0:
                truck += 1
                print("total truck +1 = {}".format(str(truck)))
                myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_truck2.config(text="{}".format(truck))
                pos_x_truck += 60
                Label_truck = Label(win,text='truck_image',image=truck_img)
                Label_truck.place(x=pos_x_truck,y=700)
                truck_list.append(Label_truck)
                print('Total truck # in list = ', len(truck_list))
                Tk.update(win)
            elif count_down % 3 == 0:
                car += 1
                print("total car +1 = {}".format(str(car)))
                myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_car2.config(text="{}".format(car))
                pos_x_car += 30
                Label_car = Label(win,text='car_image',image=car_img)
                Label_car.place(x=pos_x_car,y=550)
                car_list.append(Label_car)
                print('Total car # in list = ', len(car_list))
                Tk.update(win)
            elif count_down % 1 == 0:
                bike += 1
                print("total bike +1 = {}".format(str(bike)))
                myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                myLabel_bike2.config(text="{}".format(bike)) 
                pos_x += 10
                Label_bike = Label(win,text='bike_image',image=bike_img)
                Label_bike.place(x=pos_x,y=350)
                bike_list.append(Label_bike)
                print('Total bike # in list = ', len(bike_list))
                Tk.update(win)
        if count_down == 61:
            change_yellow()
print("-----------SUMMARY-----------------------")
print("total = {} seconds".format(str(count_down)))
print("total bikes = {}".format(str(bike)))
print("total cars = {}".format(str(car)))
print("total truck = {}".format(str(truck)))
print('Total bike # in list = ', len(bike_list))
print('Total car # in list = ', len(car_list))
print('Total truck # in list = ', len(truck_list))
    

#Button - start
start_btn = Button(text='start', bg='green', command=start_countdown)
start_btn.grid(row=0, column=0)
#Label-traffic light img
TrafficLights_yellow_img = PhotoImage(file='C:\\Users\Bruce Ashbee\\Documents\\traffic-lights-yellow.PNG')
TrafficLights_green_img = PhotoImage(file='C:\\Users\Bruce Ashbee\\Documents\\traffic-lights-green.PNG')
TrafficLights_red_img = PhotoImage(file='C:\\Users\Bruce Ashbee\\Documents\\traffic-lights-red.PNG')
TrafficLights_label = Label(win, text="traffic_light", bg="green",image=TrafficLights_red_img)
TrafficLights_label.grid(row = 1, column=0)
#------------------------------------FOR showing numbers--------------------------------------------
#Label- bike number
myLabel_bike = Label(win, text="機車 : ")
myLabel_bike.place(x=0, y=300)
myLabel_bike2 = Label(win, text="")
myLabel_bike2.place(x=50, y=300)
#Label- car number
myLabel_car = Label(win, text="Car : ")
myLabel_car.place(x=0, y=500)
myLabel_car2 = Label(win, text="")
myLabel_car2.place(x=50, y=500)
#Label - truck number
myLabel_truck = Label(win, text="Truck : ")
myLabel_truck.place(x=0, y=680)
myLabel_truck2 = Label(win, text="")
myLabel_truck2.place(x=50, y=680)
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