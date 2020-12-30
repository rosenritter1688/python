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
    #print(content['station_name'])#? check for getting values for adding listbox selections
    my_listbox.insert(END,f"{idx:03} 站名 {content['station_name']} ph值 {content['pH_value']} 濁度 {content['turbidity']} 餘氯 {content['residual_chlorine']}")
    Tk.update(root)




def execute_SQL_command(sql_command):
    global conn
    print(sql_command)   #? for double checking each sql command
    conn.executescript(sql_command)
    conn.commit()
    #conn.close() #! if u leave it here then u will only permit to insert 1 data only
                  #! database is locked

list_station_name = []
list_pH_value = []
list_turbidity = []
list_residual_chlorine = []

def add_to_lists():
    global list_station_name,list_pH_value,list_turbidity,list_residual_chlorine
    list_station_name.append(content['station_name'])
    list_pH_value.append(content['pH_value'])
    list_turbidity.append(content['turbidity'])
    list_residual_chlorine.append(content['residual_chlorine'])

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
        #print(idx,content)
        ##62 {'station_name': '水母淨水場', 'pH_value': '7.68', 'turbidity': '0.18', 'residual_chlorine': '0.61'}
        ##63 {'station_name': '成功淨水場', 'pH_value': '7.78', 'turbidity': '0.48', 'residual_chlorine': '0.65'}
        ##64 {'station_name'.: '紅葉淨水場', 'pH_value': '8.28', 'turbidity': '0.2', 'residual_chlorine': '0.38'}
        ##65 {'station_name': '瑞豐淨水場', 'pH_value': '7.08', 'turbidity': '0.6', 'residual_chlorine': '0.42'}
        ##66 {'station_name': '關山淨水場', 'pH_value': '7.91', 'turbidity': '0.25', 'residual_chlorine': '0.53'}
        listbox_add_selection()
        add_to_lists()


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
my_listbox = Listbox(my_frame, width=110, bg="#353130",fg="white",yscrollcommand=scroll_bar_4_my_listbox.set, selectmode = MULTIPLE)  #?yscrollcommand -> is for horizontal scrollbar
my_listbox.grid(row=0,column=0,sticky=W+E)

scroll_bar_4_my_listbox.config(command=my_listbox.yview)

def sql_add_DB():
    global conn
    global list_station_name,list_pH_value,list_turbidity,list_residual_chlorine
    global idx
    sql_command = " INSERT INTO water (station_name, pH_value, turbidity, residual_chlorine) values("
    sql_command = sql_command + "'" + list_station_name[idx] + "'" + "," + list_pH_value[idx] + ","  + list_turbidity[idx] + ","  + list_residual_chlorine[idx] + ")"
    print(sql_command)
    conn.executescript(sql_command)
    conn.commit()  

def insert_to_DB():
    
    global list_station_name,list_pH_value,list_turbidity,list_residual_chlorine
    global idx
    print(my_listbox.curselection()) #? listbox 編號是從0開始 跟LIST依樣
    ## (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65)
    # for item in my_listbox.curselection():              #!   item    is for each time we loop we get the index of the list box
    #     print(str(item))
        # selected_options = selected_options + my_listbox.get(item) + "\n"  #?my_listbox.get() -> get the index we want to get
        # ## terminal (0, 1, 2) Label ( one "\n" two  "\n" three "\n"  ) #! line at 65 , label will get the text of the selected lists 
        # selected_options = selected_options + str(item) + "\n"   #! label will get index number of the selected lists
        # ## terminal (0, 1, 2) Label ( 0 "\n" 1  "\n" 2 "\n"  )
    '''double checking
    # print(len(list_station_name))
    # print(len(list_pH_value))
    # print(len(list_turbidity))
    # print(len(list_residual_chlorine))
    # print(list_station_name)
    # print(list_pH_value)
    # print(list_turbidity)
    # print(list_residual_chlorine)
    '''
    for idx in my_listbox.curselection():
        '''檢查是否可以正確拿到編號和資料
        print(idx)
        print(list_station_name[idx])
        print(list_pH_value[idx])
        print(list_turbidity[idx])
        print(list_residual_chlorine[idx])
        '''
        sql_add_DB()

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
my_listbox2 = Listbox(my_frame2, width=110, bg="#353130",fg="white",yscrollcommand=scroll_bar_4_my_listbox2.set, selectmode = MULTIPLE)  #?yscrollcommand -> is for horizontal scrollbar
my_listbox2.grid(row=0,column=0,sticky=W+E)

scroll_bar_4_my_listbox.config(command=my_listbox2.yview)

root.mainloop()

