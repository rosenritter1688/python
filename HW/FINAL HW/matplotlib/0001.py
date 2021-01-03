# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:41:21 2020
@author: Administrator
"""
from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
import sqlite3
import numpy
#from pandas import DataFrame
import matplotlib.pyplot as plt
import sys
import os
import matplotlib.font_manager as fm

 

import pandas as pd

 

from matplotlib.font_manager import FontProperties

 

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
win.geometry('1900x800')
#-------

 

def qo(instr):
     return "'" + instr + "'"
def getAll():
    sqlstr = "select std_id, course_id, rcd from record "
    listx = execSQLcommand(sqlstr).fetchall()
    resultList.delete(0, END)
    for item in listx:
        resultList.insert(0, item)

 

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

 


#----
def getAvg():
    #處理字形
# =============================================================================
#     if sys.platform == 'win32':
#        fpath = 'C:\\Windows\\Fonts\\kaiu.ttf'
#     elif sys.platform.startswith('linux'):
#        basedir = '/usr/share/fonts/truetype'
#        fonts = ['freefont/FreeSansBoldOblique.ttf', 'ttf-liberation/LiberationSans-BoldItalic.ttf',              'msttcorefonts/Comic_Sans_MS.ttf']
#        for fpath in fonts:
#            if os.path.exists(os.path.join(basedir, fpath)):
#               break
#     else:
#        fpath = '/Library/Fonts/Tahoma.ttf'
# 
#     if os.path.exists(fpath):
#        prop = fm.FontProperties(fname=fpath)
#        fname = os.path.split(fpath)[1]
#        
#     else:
#        ax.set_title('Demo fails--cannot find a demo font')
# =============================================================================
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #! 中文才不會亂碼 
    plt.rcParams['axes.unicode_minus'] = False   #! 中文才不會亂碼
    # sqlstr = "select c.course_name as course_name, avg(r.rcd) as avgRcd"
    # sqlstr += "  from course c, record r "
    # sqlstr += " where r.course_id = c.course_id "
    # sqlstr += " group by c.course_name "

    sqlstr = "select std_id, avg(rcd) from record"
    sqlstr += " group by std_id "
    listx = execSQLcommand(sqlstr).fetchall()
    #產生Dictionary-------
    #dictx = {}
    std_id_list = []
    avgList=[]
    for item in listx:
        print(item)
        #dictx[item[0]] = item[1]
        std_id_list.append(item[0])
        avgList.append(item[1])
        
    #產生Dataframe-------
    myDframe = pd.DataFrame({'std_id':std_id_list, 'avgRcd':avgList})
    
    #df = pd.DataFrame({'t':t, 's':np.sin(2*np.pi*t)})
    #print('-->', courseList)
    #print('-->', avgList)
    
    #產生Figuration-----
    fig = Figure(figsize = (10, 5),  dpi = 100 ) 
    plot1 = fig.add_subplot(111) 
    plot1.set_xlabel('每個學生的平均分數') #plot1.set_xlabel('各科目平均分數', fontproperties=prop)
    
    #
    #plot1.plot(x, y1)  
    #plot1.plot(x, y2, linestyle='-', color='r')
    #myDframe.plot(x='std_id',  y='avgRcd',  ax=plot1, kind='scatter')
    myDframe.plot(x='std_id',  y='avgRcd',  ax=plot1)
    #myDframe.plot(avgList,  kind='pie',labels=courseList,explode=explode, autopct='%1.1f%%',counterclock=False, shadow=True)

 

    #plot1.plot(myDframe)
    #plot1.legend()
    #plot1.grid()
    #
    canvas = FigureCanvasTkAgg(fig, master = win)   
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=3)
    
btnGetStat = Button(win, text='科目平均', command=getAvg)
btnGetStat.grid(row=2, column=0, columnspan=2 ,sticky=S+W+E)

 

win.mainloop()