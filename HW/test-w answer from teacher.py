import sqlite3
from tkinter import Text,Button,END,Scrollbar,Tk
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
      
win=Tk()
win.geometry("800x500")
win.config(bg='lightblue')
      
myConn = sqlite3.connect("C:\\Users\\Administrator\\Desktop\\student.db")
myCursor = myConn.cursor()

 

#select data

 

def go():
   
    resultList = execSQLcommand(sqlstr).fetchall()
    print(resultList)
    for idx, std in enumerate(resultList, 0):
        result.insert(END, '學號:{0},姓名:{1},性別:{2}\n'.format(std[0], std[1], std[2]))
sqlcommand = Text(win, width=50, height=5)
sqlcommand.grid(row=0, column=0, sticky=W+E)    
scroll = Scrollbar(win, command=sqlcommand.yview)
scroll.grid(row=0, column=1, sticky = N+S)

 

execommand = Button(win, text='執行', command=go)
execommand.grid(row=1, column=0, columnspan=3, sticky=W+E)  

 

result = Text(win)
result.grid(row=2, column=0)
scrollx = Scrollbar(win, command=result.yview)
scrollx.grid(row=2, column=1, sticky = N+S)
sqlstr = " select * from student "
sqlcommand.insert(1.0, sqlstr)
#-----------------------

 

#------------------------
win.mainloop()
 