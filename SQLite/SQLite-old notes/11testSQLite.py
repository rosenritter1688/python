
 

 

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:45 2019

@author: clark
"""

from tkinter import *
import sqlite3

myConn = sqlite3.connect("student.db")

def getSQLresult(sqlstr):
    resultset = myConn.execute(sqlstr).fetchall() #fetch all rows from resultest
    """
    .fetchall()
    http://c.biancheng.net/view/2573.html
    Python（SQLite）fetchone()、fetchmany()和fetchall()用法
    
    """
    return resultset

def getAllStudent():
    sqlstr = " select std_id, Std_Name, dep_id, sex,  religion, birth_place, birthday "  ##SELECT   
    sqlstr += "  from student"  # COMPANY 表中獲取並顯示記錄：
    
    #myset = list()
    myset = getSQLresult(sqlstr)  #myset = def getSQLresult(sqlstr)  Line 8

    datalist.delete(0,END)        #Line 123  datalist = Listbox(win)
    for idx, item in enumerate(myset, 0):   # 下標從 1 開始   --->這邊應該不用打,0
        datalist.insert(END,"{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(item[0],item[1], item[2], item[3], item[4], item[5], item[6]))
'''
enumerate

實例

以下展示了使用 enumerate() 方法的實例：

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(enumerate(seasons, start=1))       # 下標從 1 開始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


普通的 for 循環
i = 0
seq = ['one', 'two', 'three']
for element in seq:
     print i, seq[i]
     i +=1
 
###0 one
###1 two
###2 three
     
for 循環使用 enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
     print i, element
 
###0 one
###1 two
###2 three

'''        
#x = ('apple', 'banana', 'cherry')
#y = enumerate(x)
#print(list(y))
###[(0, 'apple'), (1, 'banana'), (2, 'cherry')] 

def getitem(evt):
    selecteditem = datalist.get(datalist.curselection()[0])
    selectedlist = selecteditem.split('-')
    #=== std_id ===
    std_id = selectedlist[0]
    estd_id.delete(0,END)
    estd_id.insert(0,std_id)
    #=== dep_id ===
    dep_id = selectedlist[2]
    #  判斷Option Mennu停在哪喇
    for idx, item in enumerate( depset,0):
        if dep_id == (item.split(':'))[0]:
            depvar.set(item)
            break
    #== sex ==    
    varSex.set(selectedlist[3])
    #-----信仰-----
    religion = selectedlist[4]
    ereligion.delete(0,END)
    ereligion.insert(END, religion)
    #-----出生地-----
    birth_place = selectedlist[5]
    ebirth_place.delete(0,END)
    ebirth_place.insert(END, birth_place)
    #-----生日-----
    birthday = selectedlist[6]
    ebirthday.delete(0,END)
    ebirthday.insert(END, birthday)
def preparedepList():
    sqlstr =  'select dep_id, Dep_Name'
    sqlstr += ' from department '
    temp = getSQLresult(sqlstr)
    for idx , item in enumerate(temp,0):
        depset.append("{0}:{1}".format(item[0], item[1]))

def getSexValue():
    print("sex:",  varSex.get() )
    
win = Tk()
win.geometry("600x520")
win.config(background="lightyellow")
#-------
   
    

    
queryStd = Button(win)
queryStd.config(text="全部學生", bg="gray", fg="white", width=10, height=2, font="標楷體14", command=getAllStudent)  #Line 22 def getAllStudent()
queryStd.grid(row=0, column=0, stick=W)
#--------
datalist = Listbox(win)  ##全部學生按鈕下面的LIST BOX
datalist.bind('<<ListboxSelect>>', getitem)
datalist.config(width=80, height=15)
datalist.grid(row=1, column=0, columnspan=4)

#------
myScrollbar = Scrollbar(win)
myScrollbar.grid(row=1, column=4, stick=N+S)
myScrollbar.config(command=datalist.yview)
#====================================================
#學號--------------------------
lstd_id = Label(win, text="Std_Id")
lstd_id.grid(row=2, column=0)
estd_id = Entry(win)
estd_id.grid(row=2, column=1, stick=W+E)
#姓名----------------------------
lstd_name = Label(win, text="Std Name")
lstd_name.grid(row=2, column=2)
estd_name = Entry(win)
estd_name.grid(row=2, column=3, stick=W+E)
#學系-----------------------------
ldepartment = Label(win, text="學系")
ldepartment.grid(row=3, column=0)
depset = list()
preparedepList()
depvar = StringVar() #準備 反映點選項目
depvar.set(depset[0]) #預設depList停駐的index

depList  = OptionMenu(win, depvar, *depset)
depList.grid(row=3, column=1, stick=W+E)
#性別----------------------------

lsex = Label(win, text="性別")
lsex.grid(row=3, column=2)
sexFrame = Frame(win)
sexFrame.grid(row=3, column=3, stick=W+E)

varSex = StringVar()
radioM = Radiobutton(sexFrame,text="男", variable=varSex, value = "M", command=getSexValue)
radioM.grid(row=0, column=0, sticky=W)
radioF = Radiobutton(sexFrame,text="女", variable=varSex, value = "F", command=getSexValue)
radioF.grid(row=0, column=1, sticky=W)

#---信仰----
lreligion = Label(win, text="信仰")
lreligion.grid(row=4, column=0)
ereligion = Entry(win)
ereligion.grid(row=4, column=1, stick=W+E)
#--生日---
lbirthday = Label(win, text="生日")
lbirthday.grid(row=4, column=2)
ebirthday = Entry(win)
ebirthday.grid(row=4, column=3, stick=W+E)

 #--生日---
lbirth_place = Label(win, text="居住地")
lbirth_place.grid(row=5, column=2)
ebirth_place = Entry(win)
ebirth_place.grid(row=5, column=3, stick=W+E)

#=====================
opFrame = Frame(win)
opFrame.grid(row=6, column=0, columnspan=4, stick=W+E)
#
opInsert = Button(opFrame)
opInsert.config(text="新增", bg="gray", fg="blue", width=10, height=2, font="標楷體14")
opInsert.grid(row=0, column=0, stick=W+E)
#
opUpdate = Button(opFrame)
opUpdate.config(text="修改", bg="gray", fg="blue", width=10, height=2, font="標楷體14")
opUpdate.grid(row=0, column=1, stick=W+E)
#
opDelete = Button(opFrame)
opDelete.config(text="刪除", bg="gray", fg="blue", width=10, height=2, font="標楷體14")
opDelete.grid(row=0, column=2, stick=W+E)

win.mainloop() 