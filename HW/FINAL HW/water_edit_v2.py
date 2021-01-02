
#!TODO adding with function

import sqlite3
from tkinter import * #Listbox,END,Button,ANCHOR,Label,Frame,Scrollbar,VERTICAL,RIGHT,Y,Tk,MULTIPLE,Entry
import tkinter as tk


edit = tk.Tk()
edit.geometry("1000x940")                  #Width x Height
edit.config(bg="#353130")                  #背景
edit.title("water_read")              
edit.resizable(1,1)                        #1:True 0:False  此例 寬不可調, 高可調
edit.maxsize(width=1500, height=1080)      #可調整最大尺寸
#edit.minsize(width=800, height=640)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico                 
edit.attributes("-alpha",1)                #透明度:0(全透)到1(不透)之間 
edit.attributes("-topmost",True)           #出現在螢幕最上面

with sqlite3.connect(r'C:\Users\Bruce Ashbee\Documents\Python\HW\FINAL HW\myData.db') as conn:
    c = conn.cursor()


label_station_name= Label(edit,text="淨水廠名稱",bg="#353130",fg="white")
label_station_name.grid(row=0,column=0)
label_pH_value= Label(edit,text="PH值",bg="#353130",fg="white")
label_pH_value.grid(row=1,column=0)
label_turbidity= Label(edit,text="濁度",bg="#353130",fg="white")
label_turbidity.grid(row=2,column=0)
label_residual_chlorine= Label(edit,text="餘氯",bg="#353130",fg="white")
label_residual_chlorine.grid(row=3,column=0)

entry_station_name = Entry(edit,width=100,bg="#353130",fg="white")
entry_station_name.grid(row=0,column=1,columnspan=2,sticky="WE")
entry_ph_value = Entry(edit,width=100,bg="#353130",fg="white")
entry_ph_value.grid(row=1,column=1,columnspan=2,sticky="WE")
entry_turbidity = Entry(edit,width=100,bg="#353130",fg="white")
entry_turbidity.grid(row=2,column=1,sticky="WE")
entry_residual_chlorine = Entry(edit,width=100,bg="#353130",fg="white")
entry_residual_chlorine.grid(row=3,column=1,sticky="WE")

list_station_name = []
list_ph_value = []
list_turbidity = []
list_residual_chlorine = []



def check_DB():
    global content
    global list_station_name,list_ph_value,list_turbidity,list_residual_chlorine
    my_listbox.delete(0,END) #? delete all
    Tk.update(edit)
    global c
    print ("Opened database successfully")
    cursor = c.execute("SELECT *  from water")
    for idx, content in enumerate(cursor, 1):
        my_listbox.insert(END,f"{str(idx)} {content[0]} {content[1]} {content[2]} {content[3]}")
        Tk.update(edit)
        list_station_name.append(content[0])
        list_ph_value.append(content[1])
        list_turbidity.append(content[2])
        list_residual_chlorine.append(content[3])
    
    '''double checking
    print(len(list_station_name))
    print(len(list_pH_value))
    print(len(list_turbidity))
    print(len(list_residual_chlorine))
    '''
    

def insert_DB():
    station_name = entry_station_name.get()
    ph_value = entry_ph_value.get()
    turbidity =entry_turbidity.get()
    residual_chlorine = entry_residual_chlorine.get()
    #print("station_name : " + station_name,"ph_value : " + ph_value,"turbidity : " + turbidity,"residual_chlorine : " + residual_chlorine)
    global conn
    sql_command = " INSERT INTO water (station_name, pH_value, turbidity, residual_chlorine) values("
    sql_command = sql_command + "'" + station_name + "'" + "," + ph_value + ","  + turbidity + ","  + residual_chlorine + ")"
    print(sql_command)
    conn.executescript(sql_command)
    #conn.commit()  

insert_btn = Button(edit,command=insert_DB,width=15,text="INSERT",bg="#353130",fg="white")
insert_btn.grid(row=0,column=2,sticky="WE")

def update_DB():
    SELECT ROW_NUMBER() AS num_row FROM water
    global value_frm_listbox #?its from def pass_selected_value_frm_listbox_to_entry
    #id_number_in_DB += 1
    station_name2 = entry_station_name.get()
    ph_value2 = entry_ph_value.get()
    turbidity2 =entry_turbidity.get()
    residual_chlorine2 = entry_residual_chlorine.get()
    # c.execute(f"""UPDATE water
    #              SET station_name = {station_name2}, pH_value = {ph_value2},turbidity = {turbidity2},residual_chlorine = {residual_chlorine2}
    #              Where station_name = {station_name2}
    #              """)
update_btn = Button(edit,command=update_DB,width=15,text="UPDATE",bg="#353130",fg="white")
update_btn.grid(row=1,column=2,sticky="WE")

def delete_DB():
    pass
delete_btn = Button(edit,command=delete_DB,width=15,text="DELETE",bg="#353130",fg="white")
delete_btn.grid(row=2,column=2,sticky="WE")


query_btn= Button(edit,command=check_DB,width=15,text="QUERY",bg="#353130",fg="white")
query_btn.grid(row=4,column=0,columnspan=4,sticky="WE")


def pass_selected_value_frm_listbox_to_entry(event):
    global list_station_name,list_ph_value,list_turbidity,list_residual_chlorine
    #? my_listbox.bind('<<ListboxSelect>>',left_click) this line of coding is a must!!!!!!!! at line 117
    entry_station_name.delete(0, END)
    entry_ph_value.delete(0, END)
    entry_turbidity.delete(0, END)
    entry_residual_chlorine.delete(0, END)
    #! method 1 get selected value from list box
    # value = (my_listbox.get(ANCHOR))
    # print(value)
    ## 8 龍潭淨水場 7.95 0.28 0.6
    #! method 2
    # widget = event.widget
    # selection=widget.curselection()
    # print(selection)
    # ## (1,)
    # print(type(selection))
    # ##<class 'tuple'>
    #! method 3
    value = (my_listbox.curselection())
    #print(value)
    ##(3,)
    #print(type(value))
    ##<class 'tuple'>
    value_frm_listbox = value[0]
    print(f"value frm list box is {value_frm_listbox}")
    ## 3
    #print(list_station_name[value_frm_listbox])
    ##坪林淨水場
    entry_station_name.insert(1,f"{list_station_name[value_frm_listbox]}")
    entry_ph_value.insert(1,f"{list_ph_value[value_frm_listbox]}")
    entry_turbidity.insert(1,f"{list_turbidity[value_frm_listbox]}")
    entry_residual_chlorine.insert(1,f"{list_residual_chlorine[value_frm_listbox]}")
    return value_frm_listbox



#? Frame1
my_frame = Frame(edit)
my_frame.grid(row=5,column=0,columnspan=4,sticky=W+E)

#scroll bar
scroll_bar_4_my_listbox = Scrollbar(my_frame,orient=VERTICAL)
scroll_bar_4_my_listbox.grid(row=0,column=1,sticky="NS")

#Listbox
#*  SELECT MODE = SINGLE IS AT DEFAULT
my_listbox = Listbox(my_frame, width=123, bg="#353130",fg="white",yscrollcommand=scroll_bar_4_my_listbox.set)  #?yscrollcommand -> is for horizontal scrollbar  #!selectmode = MULTIPLE 
my_listbox.grid(row=0,column=0,columnspan=3,sticky=W+E)
my_listbox.bind('<<ListboxSelect>>',pass_selected_value_frm_listbox_to_entry) #! 滑鼠左鍵點一次之後呼叫功能pass_selected_value_frm_listbox_to_label
#! <Button-1> 表示滑鼠左鍵按一次，可是用的話會顯示上一個所選的  所以要改用<<ListboxSelect>>  才會顯示現在所選的選項
scroll_bar_4_my_listbox.config(command=my_listbox.yview)

edit.mainloop()

