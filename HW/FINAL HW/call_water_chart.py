from tkinter import * #Listbox,END,Button,ANCHOR,Label,Frame,Scrollbar,VERTICAL,RIGHT,Y,Tk,MULTIPLE,Entry
import tkinter as tk

chart = tk.Tk()
chart.geometry("1000x940")                  #Width x Height
chart.config(bg="#353130")                  #背景
chart.title("FINAL HW")              
chart.resizable(1,1)                        #1:True 0:False  此例 寬不可調, 高可調
chart.maxsize(width=1500, height=1080)      #可調整最大尺寸
#main.minsize(width=800, height=640)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico                 
chart.attributes("-alpha",1)                #透明度:0(全透)到1(不透)之間 
chart.attributes("-topmost",True)           #出現在螢幕最上面

import sqlite3

with sqlite3.connect(r'C:\Users\Bruce Ashbee\Documents\Python\HW\FINAL HW\myData.db') as myConn:
    myCursor = myConn.cursor()

def execSQLcommand(sqlstr):
    global myConn
    global myCursor
    try:
      myCursor = myConn.execute(sqlstr)
      myConn.commit()
      print("指令已成功執行:" + sqlstr)
      return myCursor
    except:
      print("指令有誤:", sqlstr)

def getStat():
    sqlstr = "select std_id , rcd from record  where course_id = 'C001'"
    '''
    #select std_id , rcd from record  where course_id = 'C001';
    select std_id , rcd from record  where course_id = 'C002';
    select std_id , rcd from record  where course_id = 'C003';
    '''
    result = execSQLcommand(sqlstr).fetchall()
    C001_stdList = []
    #C001_courseList = []
    C001_rcdList = []
    for item in result:
        
        C001_stdList.append(item[0])
        #courseList.append(item[1])
        C001_rcdList.append(item[1])
    sqlstr = "select std_id , rcd from record  where course_id = 'C002'"
    '''
    #select std_id , rcd from record  where course_id = 'C001';
    #select std_id , rcd from record  where course_id = 'C002';
    select std_id , rcd from record  where course_id = 'C003';
    '''
    result = execSQLcommand(sqlstr).fetchall()
    C002_stdList = []
    #C001_courseList = []
    C002_rcdList = []
    for item in result:
        C002_stdList.append(item[0])
        #courseList.append(item[1])
        C002_rcdList.append(item[1])
    sqlstr = "select std_id , rcd from record  where course_id = 'C003'"
    result = execSQLcommand(sqlstr).fetchall()
    C003_stdList = []
    #C001_courseList = []
    C003_rcdList = []
    for item in result:
        C003_stdList.append(item[0])
        #courseList.append(item[1])
        C003_rcdList.append(item[1])
    fig = Figure(figsize = (5, 5),  dpi = 100)  #1.設定Figure
    plot1 = fig.add_subplot(111) #2.設定subplot(子圖)
    plot1.plot(C001_rcdList, 'b', label="C001") #3.在子圖畫圖(plot)
    plot1.plot(C002_rcdList, "x-r", label="C002")
    plot1.plot(C003_rcdList, "x-.c", label="C003")
    #mp.plot(data2, "o--b", label="data2")
    ####mp.plot(data3, "s--c", label="data3")
    #? ignore this first plot1.plot(y2,'r')
    canvas = FigureCanvasTkAgg(fig, master = win) #4.設定canvas並將Figure貼上
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=5) #5.將canvas貼在window
 

btnStat = Button(chart, text='統計', command=getStat)
btnStat.grid(row=5, column=0, columnspan=3, sticky=W+E)

chart.mainloop()