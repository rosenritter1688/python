#HW in class
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:41:21 2020

 

@author: Administrator
"""
import matplotlib.pyplot as mp
import numpy as np
from tkinter import *

 

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

 


import sqlite3
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
myConn = sqlite3.connect(r"C:\Users\Bruce Ashbee\Documents\Python\HW\SENSEI\student.db")
myCursor = myConn.cursor()

 

win = Tk()
win.geometry('800x800')
#-------
lblstd_id = Label(win, text='Student ID')
lblstd_id.grid(row=0, column=0)
def getStdId(selection):
    selectedStdItem.set(selection[0]) # std_id
selectedStdItem = StringVar()
sqlstr = "select std_id , std_name from student "
stddata = execSQLcommand(sqlstr).fetchall()

 

stdList = OptionMenu(win, selectedStdItem, *stddata, command=getStdId)
stdList.grid(row=0, column=1, sticky=W+E)
#--------
lblcourse_id = Label(win, text='Course ID')
lblcourse_id.grid(row=1, column=0)
def getCourseId(selection):
    selectedCourseItem.set(selection[0]) # course_id
selectedCourseItem = StringVar()
sqlstr = "select course_id , course_name from course "
coursedata = execSQLcommand(sqlstr).fetchall()

 

courseList = OptionMenu(win, selectedCourseItem, *coursedata, command=getCourseId)
courseList.grid(row=1, column=1, sticky=W+E)

 


lblrcd = Label(win, text='record')
lblrcd.grid(row=2, column=0)
etyrcd=Entry(win)
etyrcd.grid(row=2, column=1)
def  qo(instr):
     return "'" + instr +"'"
def getAll():
    sqlstr = "select std_id, course_id, rcd from record "
    listx = execSQLcommand(sqlstr).fetchall()
    resultList.delete(0, END)
    for item in listx:
        resultList.insert(0, item)
def doInsert():
    sqlstr = "insert into record(std_id, course_id, rcd)"
    sqlstr += "values(" + qo(selectedStdItem.get()) + ","
    sqlstr +=  qo(selectedCourseItem.get()) + ","
    sqlstr +=  etyrcd.get() + ")"
    print(sqlstr)
    execSQLcommand(sqlstr)
    getAll()
def doUpdate():
    sqlstr = " update course set"
    sqlstr += " course_name = " + qo(etycourse_name.get())
    sqlstr += ", credit = " + etycredit.get()
    sqlstr += " where course_id = " + qo(etycourse_id.get())
    execSQLcommand(sqlstr)
    getAll()
def doDelete():
    sqlstr = " delete from course"
    sqlstr += " where course_id = " + qo(etycourse_id.get())
    execSQLcommand(sqlstr)
    getAll()
btnInsert = Button(win, text='Insert', fg='blue', command=doInsert)
btnInsert.grid(row=0,column=2, sticky=W+E)
btnUpdate = Button(win, text='Update', fg='blue', command=doUpdate)
btnUpdate.grid(row=1,column=2, sticky=W+E)
btnDelete = Button(win, text='Delete', fg='blue', command=doDelete)
btnDelete.grid(row=2,column=2, sticky=W+E)

 

def onselect(evt):
    idx = resultList.curselection()[0]
    selecteditem = resultList.get(idx) #tuple selected
    print("點選內容", selecteditem)
    
    etycourse_id.delete(0, END);  
    etycourse_id.insert(0, selecteditem[0] )

 

    etycourse_name.delete(0, END); 
    etycourse_name.insert(0, selecteditem[1] )
    
    etycredit.delete(0, END); 
    etycredit.insert(0, selecteditem[2] )

 


resultList = Listbox(win)
resultList.grid(row=3, column=0, columnspan=3, sticky=W+E)
resultList.bind('<<ListboxSelect>>', onselect)

 

btnSelectAll = Button(win, text='Query', command=getAll)
btnSelectAll.grid(row=4, column=0, columnspan=3, sticky=W+E)

#! one line in chart here
# def getStat():
#     #sqlstr = "select std_id , avg(rcd) from record  group by std_id "
#     #? try select std_id , rcd from record  where course_id = 'C001'
#     sqlstr = "select std_id , rcd from record  where course_id = 'C001'"
#     result = execSQLcommand(sqlstr).fetchall()
#     stdList = []
#     courseList = []
#     rcdList = []
#     for item in result:
        
#         stdList.append(item[0])
#         #courseList.append(item[1])
#         rcdList.append(item[1])
#     fig = Figure(figsize = (5, 5),  dpi = 100)  #1.設定Figure
#     plot1 = fig.add_subplot(111) #2.設定subplot(子圖)
#     plot1.plot(rcdList, 'b') #3.在子圖畫圖(plot)
#     #? ignore this first plot1.plot(y2,'r')
#     canvas = FigureCanvasTkAgg(fig, master = win) #4.設定canvas並將Figure貼上
#     canvas.get_tk_widget().grid(row=6, column=0, columnspan=5) #5.將canvas貼在window
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
    print("result is : " ,result)
    ## [('梁', 98), ('S002', 85), ('S003', 98), ('S004', 67), ('S005', 60), ('S006', 62), ('S007', 85), ('S008', 65), ('S009', 81), ('S010', 76), ('S011', 70), ('S012', 93), ('S013', 93), ('S014', 83), ('S015', 95), ('S016', 64), ('S017', 55), ('S018', 93), ('S019', 51), ('S020', 55), ('S021', 75), ('S022', 88), ('S023', 69), ('S024', 83), ('S025', 96), ('S026', 72), ('S027', 86), ('S028', 96), ('S029', 81), ('S030', 76)]
    ##[98, 85, 98, 67, 60, 62, 85, 65, 81, 76, 70, 93, 93, 83, 95, 64, 55, 93, 51, 55, 75, 88, 69, 83, 96, 72, 86, 96, 81, 76]
    for item in result:
        
        C001_stdList.append(item[0])
        #courseList.append(item[1])
        C001_rcdList.append(item[1])
    print(C001_rcdList)
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
 

btnStat = Button(win, text='統計', command=getStat)
btnStat.grid(row=5, column=0, columnspan=3, sticky=W+E)

 

win.mainloop()