import sqlite3
from tkinter import Tk,Button,END
import tkinter as tk
root = tk.Tk()
root.geometry("600x640")
root.config(bg="#353130")



'''#!working MAC



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
    result=textbox_example.get("1.0","end")#?retrive text from textbox and name content as result
    #<WIN>#
    # with sqlite3.connect("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\SQLite\\std.db") as datafile_readed:
    #<MAC>
    with sqlite3.connect("//Users//bruceashbee//Documents//SQLite//std.db") as datafile_readed:
        result = datafile_readed.execute(f" {result} ").fetchall()#? fetchall() get all data
        print(result,"\n",type(result)) #? content of the list are full of tuple
        ##<class 'list'>
        for index, content_each_tuple in enumerate(result, 0):   #? indexing result從0開始給
            print(index, content_each_tuple)      #! result is a list!!!! contents of list are tuple
            textbox_show.insert(END,(index, content_each_tuple,"\n"))   
                            #! (1.0,index,content_each_tuple) #its not working this way      
                            #!  如果要丟進去的變數不只一個就要用括號刮起來    
    #textbox_example.delete("1.0","end")   #?delete text in the textbox_example 
    #print(result)
    #textbox_show.delete("1.0","end")       #? delete text in textbox_show first
    #textbox_show.insert(1.0,result)        #? pass data to textbox 



textbox_example=tk.Text(root, height=10,width=30,bg="#353130",fg="white")
textbox_example.grid(row=0,column=0)

scrollbar_4_textbox_example = tk.Scrollbar(root)
scrollbar_4_textbox_example.grid(row=0, column=1, sticky="NS")

btnRead=tk.Button(root, height=1, width=10,bg="#353130",fg="black", text="Read",command=getTextInput)
btnRead.grid(row=1,column=0,sticky="WE",columnspan=2)

textbox_show=tk.Text(root, height=10,width=30,bg="#353130",fg="white")
textbox_show.grid(row=2,column=0)

scrollbar_4_textbox_show = tk.Scrollbar(root)
scrollbar_4_textbox_show.grid(row=2, column=1, sticky="NS")

root.mainloop()