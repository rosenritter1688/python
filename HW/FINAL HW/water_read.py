import requests
import json
import sqlite3
from tkinter import * #Listbox,END,Button,ANCHOR,Label,Frame,Scrollbar,VERTICAL,RIGHT,Y,Tk,MULTIPLE,Entry
import tkinter as tk

root = tk.Tk()
root.geometry("1000x940")                  #Width x Height
root.config(bg="#353130")                  #背景
root.title("FINAL HW")              
root.resizable(1,1)                        #1:True 0:False  此例 寬不可調, 高可調
root.maxsize(width=1500, height=1080)      #可調整最大尺寸
#root.minsize(width=800, height=640)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico                 
root.attributes("-alpha",1)                #透明度:0(全透)到1(不透)之間 
root.attributes("-topmost",True)           #出現在螢幕最上面
print("https://quality.data.gov.tw/dq_download_json.php?nid=133578&md5_url=ac39a7025bb0581ceb2eec2a28199191")

#! WIN DESTOP
conn = sqlite3.connect(r'C:\Users\Bruce Ashbee\Documents\Python\HW\FINAL HW\myData.db')
#! MAC



url_label= Label(root,text="URL :",bg="#353130",fg="white")
url_label.grid(row=0,column=0)

url_entry = Entry(root,width=100,bg="#353130",fg="white")
url_entry.grid(row=0,column=1,sticky="WE")

def listbox_add_selection():
    global content
    print(content['station_name'])#? check for getting values for adding listbox selections
    my_listbox.insert(END,f"{str(idx)} 站名 {content['station_name']} ph值 {content['pH_value']} 濁度 {content['turbidity']} 餘氯 {content['residual_chlorine']}")
    Tk.update(root)




def execute_SQL_command(sql_command):
    global conn
    print(sql_command)   #? for double checking each sql command
    conn.executescript(sql_command)
    conn.commit()
    #conn.close() #! if u leave it here then u will only permit to insert 1 data only
                  #! database is locked

def get_JSON_frm_internet():
    global content,idx
    url = url_entry.get()
    response = requests.get(url)
    jsonData = response.json()
    #print(type(jsonData))
    ## <class 'list'>
    #print(jsonData)
    ##[{'station_name': '貢寮淨水場', 'pH_value': '6.99', 'turbidity': '0.03', 'residual_chlorine': '0.77'}, {'station_name': '平溪淨水場', 'pH_value': '7.54', 'turbidity': '0.75', 'residual_chlorine': '0.58'}, {'station_name': '坪林淨水場',
    for idx, content in enumerate(jsonData,1):
        listbox_add_selection()
        #print(idx,content)
        ##62 {'station_name': '水母淨水場', 'pH_value': '7.68', 'turbidity': '0.18', 'residual_chlorine': '0.61'}
        ##63 {'station_name': '成功淨水場', 'pH_value': '7.78', 'turbidity': '0.48', 'residual_chlorine': '0.65'}
        ##64 {'station_name'.: '紅葉淨水場', 'pH_value': '8.28', 'turbidity': '0.2', 'residual_chlorine': '0.38'}
        ##65 {'station_name': '瑞豐淨水場', 'pH_value': '7.08', 'turbidity': '0.6', 'residual_chlorine': '0.42'}
        ##66 {'station_name': '關山淨水場', 'pH_value': '7.91', 'turbidity': '0.25', 'residual_chlorine': '0.53'}
        content_values = content.values() #? 讀取dict的values
        #print(content_values)
        ##dict_values(['關山淨水場', '7.91', '0.25', '0.53'])
        sql_command = " insert into water (station_name, pH_value, turbidity, residual_chlorine) values("
        for value in content_values:
            sql_command = sql_command + f"'{value}',"
        sql_command = sql_command[0:-1] + ")"
        execute_SQL_command(sql_command)
    conn.close()
#? Bttn1
get_JSON_frm_internet_btn = Button(root,command=get_JSON_frm_internet,width=15,text="GET from URL",bg="#353130",fg="white")
get_JSON_frm_internet_btn.grid(row=1,column=0,columnspan=2,sticky="WE")

#? Frame1
my_frame = Frame(root)
my_frame.grid(row=2,column=0,columnspan=2,sticky=W+E)

#scroll bar
scroll_bar_4_my_listbox = Scrollbar(my_frame,orient=VERTICAL)
scroll_bar_4_my_listbox.grid(row=0,column=1,sticky=N+S+W)

#Listbox
#*  SELECT MODE = SINGLE IS AT DEFAULT
my_listbox = Listbox(my_frame, width=110, bg="#353130",fg="white")  #?yscrollcommand -> is for horizontal scrollbar
my_listbox.grid(row=0,column=0,sticky=W+E)

scroll_bar_4_my_listbox.config(command=my_listbox.yview)

def insert_to_DB():
    pass

#? Bttn2
insert_to_DB_btn = Button(root,command=insert_to_DB,width=15,text="GET from URL",bg="#353130",fg="white")
insert_to_DB_btn.grid(row=3,column=0,columnspan=2,sticky="WE")


#? Frame2
my_frame2 = Frame(root)
my_frame2.grid(row=4,column=0,columnspan=2,sticky=W+E)

#scroll bar
scroll_bar_4_my_listbox2 = Scrollbar(my_frame2,orient=VERTICAL)
scroll_bar_4_my_listbox2.grid(row=0,column=1,sticky=N+S+W)

#Listbox
#*  SELECT MODE = SINGLE IS AT DEFAULT
my_listbox2 = Listbox(my_frame2, width=110, bg="#353130",fg="white")  #?yscrollcommand -> is for horizontal scrollbar
my_listbox2.grid(row=0,column=0,sticky=W+E)

scroll_bar_4_my_listbox.config(command=my_listbox.yview)

root.mainloop()

