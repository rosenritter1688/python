'''
某交通路口交通工具到達狀況:
卡車:5秒鐘到達1台,  10秒離開1台
汽車:3秒鐘到達1台,   5秒離開1台
摩托車:1秒鐘到達1台, 2秒離開1台 
試用計時器, 顯示每秒交通路口的工具數量, 直到60秒為止 
'''

import time
from threading import Timer  ##!!!!

def sayHello():
    print("Hello\n")


count_down = 0
bike = 0
car = 0
truck = 0
for x in range(60):
    time.sleep(1)
    count_down += 1
    print(str(count_down) + " seconds\n")
    if (count_down % 5 == 0) & (count_down % 3 == 0) & (count_down % 1 == 0):
        truck += 1
        car += 1
        bike += 1
        print("total bike +1 = {}".format(str(bike)))
        print("total car +1 = {}".format(str(car)))
        print("total truck +1 = {}\n".format(str(truck)))
    elif (count_down % 5 == 0) & (count_down % 3 == 0):
        truck += 1
        car += 1
        print("total car +1 = {}".format(str(car)))
        print("total truck +1 = {}\n".format(str(truck)))
    elif (count_down % 5 == 0) & (count_down % 1 == 0):
        truck += 1
        bike += 1
        print("total bike +1 = {}".format(str(bike)))
        print("total truck +1 = {}\n".format(str(truck)))
    elif (count_down % 3 == 0) & (count_down % 1 == 0):
        car += 1
        bike += 1
        print("total bike +1 = {}".format(str(bike)))
        print("total car +1 = {}\n".format(str(car)))
    elif count_down % 5 == 0:
        truck += 1
        print("total truck +1 = {}\n".format(str(truck)))
    elif count_down % 3 == 0:
        car += 1
        print("total car +1 = {}\n".format(str(car)))
    elif count_down % 1 == 0:
        bike += 1
        print("total bike +1 = {}\n".format(str(bike)))

    

print("----------------------------------")
print("total = {} seconds".format(str(count_down)))
print("total bikes = {}".format(str(bike)))
print("total cars = {}".format(str(car)))
print("total truck = {}".format(str(truck)))