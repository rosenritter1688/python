import sqlite3
from sqlite3 import Error
from tkinter import Tk,Button,END
import tkinter as tk
root = tk.Tk()
root.geometry("600x640")
root.config(bg="#353130")



'''#!working
MAC

with sqlite3.connect("//Users//bruceashbee//Documents//SQLite//std.db") as datafile_readed:
    result = datafile_readed.execute(" select * from student ").fetchall()#? fetchall() get all data
    print(result,"\n",type(result)) #? content of the list are full of tuple
    for index, content_each_tuple in enumerate(result, 0):   #? indexing result從0開始給
        print(index, content_each_tuple)
'''
'''#!windows

with sqlite3.connect("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\SQLite\\std.db") as datafile_readed:
    result = datafile_readed.execute(" select * from student ").fetchall()#? fetchall() get all data
    print(result,"\n",type(result)) #? content of the list are full of tuple
    for index, content_each_tuple in enumerate(result, 0):   #? indexing result從0開始給
        print(index, content_each_tuple)

'''


def getTextInput():
    result=textbox_example.get("1.0","end") #?retrive text from textbox and name content as result
    with sqlite3.connect("//Users//bruceashbee//Documents//SQLite//std.db") as datafile_readed:
        result = datafile_readed.execute(f" {result} ").fetchall()#? fetchall() get all data
        print(result,"\n",type(result)) #? content of the list are full of tuple
        ##<class 'list'>
        for index, content_each_tuple in enumerate(result, 1):   #? indexing result從1開始給
            #print(index, content_each_tuple)      #! result is a list!!!! contents of list are tuple
            #textbox_show.insert(1.0,(index, content_each_tuple)) 
                            #! (1.0,index,content_each_tuple) #its not working this way      
                            #!  如果要丟進去的變數不只一個就要用括號刮起來              
            print(index,"ID#",content_each_tuple[0],"Name",content_each_tuple[1],"Sex",content_each_tuple[2])  
            textbox_show.insert(END,(f"{index:02d}" + " <ID#> "+ content_each_tuple[0] + " <Name> " + content_each_tuple[1] + " <Sex> " + content_each_tuple[2] + "\n"))
                               #! END insert to next line REMEMBER to import END<example at line 2>
                               #! 1.0 insert to the first line
    #textbox_example.delete("1.0","end")   #?delete text in the textbox_example 
    #print(result)
    #textbox_show.delete("1.0","end")       #? delete text in textbox_show first
    #textbox_show.insert(1.0,result)        #? pass data to textbox 



textbox_example=tk.Text(root, height=10,width=50,bg="#353130",fg="white")
textbox_example.grid(row=0,column=0)

scrollbar_4_textbox_example = tk.Scrollbar(root)
scrollbar_4_textbox_example.grid(row=0, column=1, sticky="NS")

btnRead=tk.Button(root, height=1, width=10,bg="#353130",fg="pink", text="Read",command=getTextInput)
btnRead.grid(row=1,column=0,sticky="WE",columnspan=2)

textbox_show=tk.Text(root, height=60,width=50,bg="#353130",fg="pink")
textbox_show.grid(row=2,column=0)

scrollbar_4_textbox_show = tk.Scrollbar(root)
scrollbar_4_textbox_show.grid(row=2, column=1, sticky="NS")

root.mainloop()

# select std_id ,std_name
# from student

 


# select std_name
# from student
# where std_id = 'S006'

 


# select *
# from student
# where sex = 'F'

 

# select *
# from record
# where rcd < 60

 


# select record.std_id, student.std_name,  course.course_name, record.rcd
# from record , course , student 
# where record.course_id = course.course_id
#   and record.std_id = student.std_id

 

 

 

# ----------------
# update record
# set rcd = 55
# where rcd < 50

 

# select record.std_id, student.std_name,  course.course_name, record.rcd
# from record , course , student 
# where record.course_id = course.course_id
#   and record.std_id = student.std_id

 

# ---------

 


# delete from student where std_id = 'AAAA'

 


# select * from student where std_id like 'A%'