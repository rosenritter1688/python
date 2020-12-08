import time
def change_green():
    #TrafficLights_label.configure(image=TrafficLights_green_img)
    count_down =0
    flag = "go"
    bike = 60
    car = 20
    truck = 12
    #global x
    #global pos_x
    #global pos_x_car
    #global pos_x_truck
    #global bike_list, car_list, truck_list
    while flag != "stop":
        for x in range(61):
            time.sleep(1)
            count_down += 1
            #myLabel_count_down.config(text="") ##刪除之前殘留在label的資料用
            #myLabel_count_down.config(text="{}".format(count_down))
            #Tk.update(win)
            print(str(count_down) + " seconds\n")
            if (count_down <= 61) & (flag == "go"):
                if count_down == 61:
                    flag = "stop"
                    #if count_down == 61:
                    #break
                elif (count_down % 10 == 0) & (count_down % 5 == 0) & (count_down % 2 == 0):
                    truck -= 1
                    car -= 1
                    bike -= 1
                    print("total bike -1 = {}".format(str(bike)))
                    #myLabel_bike2.config(text="")                                   ##刪除之前殘留在label的資料用
                    #myLabel_bike2.config(text="{}".format(bike))
                    #Tk.update(win)                                                  #refresh win named win 
                    print("total car -1 = {}".format(str(car)))
                    #myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_car2.config(text="{}".format(car))
                    #Tk.update(win)
                    print("total truck -1 = {}\n".format(str(truck)))
                    #myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_truck2.config(text="{}".format(truck))
                    #Tk.update(win)
                elif (count_down % 10 == 0) & (count_down % 5 == 0):
                    truck -= 1
                    car -= 1
                    print("total car -1 = {}".format(str(car)))
                    #myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_car2.config(text="{}".format(car))
                    #Tk.update(win)
                    print("total truck 11 = {}\n".format(str(truck)))
                    #myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_truck2.config(text="{}".format(truck))
                    #Tk.update(win)
                elif (count_down % 10 == 0) & (count_down % 2 == 0):
                    truck -= 1
                    bike -= 1
                    print("total bike -1 = {}".format(str(bike)))
                    #myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_bike2.config(text="{}".format(bike))
                    #Tk.update(win)
                    print("total truck -1 = {}\n".format(str(truck)))
                    #myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_truck2.config(text="{}".format(truck))
                    #Tk.update(win)
                elif (count_down % 5 == 0) & (count_down % 2 == 0):
                    car -= 1
                    bike -= 1
                    print("total bike -1 = {}".format(str(bike)))
                    #myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_bike2.config(text="{}".format(bike))
                    #Tk.update(win)
                    print("total car -1 = {}\n".format(str(car)))
                    #myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_car2.config(text="{}".format(car))
                    #Tk.update(win)
                elif count_down % 10 == 0:
                    truck -= 1
                    print("total truck -1 = {}\n".format(str(truck)))
                    #myLabel_truck2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_truck2.config(text="{}".format(truck))
                    #Tk.update(win)
                elif count_down % 5 == 0:
                    car -= 1
                    print("total car -1 = {}\n".format(str(car)))
                    #myLabel_car2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_car2.config(text="{}".format(car))
                    #Tk.update(win)
                elif count_down % 2 == 0:
                    bike -= 1
                    print("total bike -1 = {}\n".format(str(bike)))
                    #myLabel_bike2.config(text="") ##刪除之前殘留在label的資料用
                    #myLabel_bike2.config(text="{}".format(bike)) 
                    #Tk.update(win)
    while flag == 'stop':
        break
change_green()

