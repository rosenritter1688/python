# -*- coding: utf-8 -*-
import sqlite3
import tkinter as tk
from tkinter import *

win = Tk()
textbox_sql = tk.Text(win, width=20, height=20)
textbox_sql.grid(row=1, column=0, columnspan=2)
def execute_sql_command():
    global myConn
    global myCursor
    sqlstr = textbox_sql.get("1.0","end")
    try:
        myCursor = myConn.execute(sqlstr)
        myConn.commit()
        print("指令已成功執行:" + sqlstr)
        return myCursor
    except:
      print("指令有誤:", sqlstr)
#-------create database or open connection -----
#設定myConn的同時建立資料庫(if not exiested), 或打開(如果已存在)
    myConn = sqlite3.connect("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\SQLite\\std.db")
    myCursor = myConn.cursor()
#myConn = sqlite3.connect(':memory:') # Create db in memory



#select data
#sqlstr = " select * from student "
    
    print(sqlstr)
#sqlstr = ' {} '.format(x)
    resultList = execute_sql_command(sqlstr).fetchall() #? fetchall() get all data 
    print(resultList)                              #? content of the list are full of tuple
    for index, content_each_tuple in enumerate(resultList, 0):   #? index從0開始給
        print(index, content_each_tuple)




scroll_4_textbox_sql_command = Scrollbar(win)
scroll_4_textbox_sql_command.grid(row=1, column=2, sticky=N+S)

btn = Button(win, text='execute', command=execute_sql_command)
btn.grid(row=2, column=0,sticky="WE",columnspan=3)

textbox_result = tk.Text(win, width=20, height=20)
textbox_result.grid(row=3, column=0, columnspan=2)

scroll_4_textbox_result = Scrollbar(win)
scroll_4_textbox_result.grid(row=3, column=2, sticky=N+S)

# def showValue(self):
#     label1.config(text=int(scale1.get()))

# scale1 = Scale(win,orient=HORIZONTAL,from_=0, to_=100,label='x', command=showValue)
# scale1.grid(row=3, column=0,columnspan=2,sticky=W+E)

# label1 = Label(win, text='X')
# label1.grid(row=3, column=2)

# def showValue2(self):
#     label2.config(text=int(scale2.get()))
    
# scale2 = Scale(win,orient=HORIZONTAL,from_=0, to_=100,label='y', command=showValue2)
# scale2.grid(row=4, column=0,columnspan=2,sticky=W+E)

# label2 = Label(win, text='Y')
# label2.grid(row=4, column=2)

win.mainloop()
