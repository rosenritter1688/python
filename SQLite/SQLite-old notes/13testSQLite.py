
 

 

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:45 2019

@author: clark
"""

from tkinter import *
import sqlite3
from sqldb import *
db = myDB("C:\\Users\\Administrator\\Desktop\\student.db")

#myConn = sqlite3.connect("C:\\Users\\Administrator\\Desktop\\student.db")
'''
def getSQLresult(sqlstr):
    resultset = db.execute(sqlstr).fetchall()
    return resultset

def execSQLcommand(sqlstr):
    global myConn
    global myCursor
    try:
      myCursor = db.execute(sqlstr)
      myConn.commit()
      print("指令已成功執行:" + sqlstr)
      return myCursor
    except Exception as ex:
      print("指令有誤:", sqlstr, ex)

def Qo(instr):
    return "'" + instr + "'"    
'''

def getAllStudent():
    sqlstr = " select std_id, Std_Name, dep_id, sex,  religion, birth_place, birthday "
    sqlstr += "  from student"
    
    #myset = list()
    myset = db.getSQLresult(sqlstr)

    datalist.delete(0,END)
    for idx, item in enumerate(myset, 0):
        datalist.insert(END,"{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(item[0],item[1], item[2], item[3], item[4], item[5], item[6]))

def getitem(evt):
    selecteditem = datalist.get(datalist.curselection()[0])
    selectedlist = selecteditem.split('-')
    #=== std_id ===
    std_id = selectedlist[0]
    estd_id.delete(0,END)
    estd_id.insert(0,std_id)
    #=== std_name ===
    std_name = selectedlist[1]
    estd_name.delete(0,END)
    estd_name.insert(0,std_name)
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
    temp = db.getSQLresult(sqlstr)
    for idx , item in enumerate(temp,0):
        depset.append("{0}:{1}".format(item[0], item[1]))

def getSexValue():
    print("sex:",  varSex.get() )

def insertStudent():
    sqlstr = "insert into student(std_id, std_name, sex, dep_id, religion, birth_place, birthday)values("
    sqlstr += Qo(estd_id.get()) + ","
    sqlstr += Qo(estd_name.get()) + ","
    sqlstr += Qo(varSex.get()) + ","
    sqlstr += Qo(depvar.get().split(':')[0]) + ","
    sqlstr += Qo(ereligion.get()) + ","
    sqlstr += Qo(ebirth_place.get()) + ","
    sqlstr += Qo(ebirthday.get()) + ")"
    db.execSQLcommand(sqlstr)
    
    getAllStudent()
    execSQLcommand(sqlstr)
    
def deleteStudent():
    sqlstr = "delete from  student "
    sqlstr += " where std_id = " + Qo(estd_id.get())
    db.execSQLcommand(sqlstr)
    getAllStudent()
    
def updateStudent():
    sqlstr = "update student set std_name = " + Qo(estd_name.get())
    sqlstr += " where std_id = " + Qo(estd_id.get())
    #sqlstr += " where std_id = '" + estd_id.get() + "' "
    db.execSQLcommand(sqlstr)
    getAllStudent()
win = Tk()
win.geometry("600x520")
win.config(background="lightyellow")
#-------
   
    

    
queryStd = Button(win)
queryStd.config(text="全部學生", bg="gray", fg="white", width=10, height=2, font="標楷體14", command=getAllStudent)
queryStd.grid(row=0, column=0, stick=W)
#--------
datalist = Listbox(win)
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
opInsert.config(text="新增", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=insertStudent)
opInsert.grid(row=0, column=0, stick=W+E)
#
opUpdate = Button(opFrame, command=updateStudent)
opUpdate.config(text="修改", bg="gray", fg="blue", width=10, height=2, font="標楷體14")
opUpdate.grid(row=0, column=1, stick=W+E)
#
opDelete = Button(opFrame)
opDelete.config(text="刪除", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=deleteStudent)
opDelete.grid(row=0, column=2, stick=W+E)

def getttt():
    print(varS)
varS = StringVar()
varS.set("2")

ttt = OptionMenu(win, varS, "1", "2", "3", command=getttt)
ttt.grid(row=7, column=0)

win.mainloop() 