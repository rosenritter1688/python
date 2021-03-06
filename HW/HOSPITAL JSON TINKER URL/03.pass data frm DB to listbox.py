import requests
import json
import sqlite3
from tkinter import * #Listbox,END,Button,ANCHOR,Label,Frame,Scrollbar,VERTICAL,RIGHT,Y,Tk,MULTIPLE,Entry
import tkinter as tk

root = tk.Tk()
root.geometry("1000x940")                  #Width x Height
root.config(bg="#353130")                  #背景
root.title("GET JSON DATA FROM INTERNET")              
root.resizable(1,1)                        #1:True 0:False  此例 寬不可調, 高可調
root.maxsize(width=1500, height=1080)      #可調整最大尺寸
#root.minsize(width=800, height=640)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico                 
root.attributes("-alpha",1)                #透明度:0(全透)到1(不透)之間 
root.attributes("-topmost",True)           #出現在螢幕最上面

url_label = Label(root,text="URL",bg="#353130",fg="white")
url_label.config(height=1)
url_label.grid(row=1,column=0)

print("https://quality.data.gov.tw/dq_download_json.php?nid=6271&md5_url=93b5af5fe0916469b3c3d5e6bc89912f")

URL_entry = Entry(root,width=100,bg="#353130",fg="white") #! height=1  cant
#URL_entry.config()
URL_entry.grid(row=1,column=1)
#! WIN DESTOP
conn = sqlite3.connect('C:\\Users\\Bruce Ashbee\\Documents\\Python\\HW\\HOSPITAL JSON TINKER URL\\hospital.db')
#! MAC
#conn = sqlite3.connect('//Users//bruceashbee//Documents//Python//HW//HOSPITAL JSON TINKER URL//hospital.db')
def execute_SQL_command(sql_command):
    #! global sql_command
    #! SyntaxError: name 'sql_command' is parameter and global
    global conn
    print(sql_command)   #? for double checking each sql command
    conn.executescript(sql_command)
    conn.commit() 
    #conn.close() #! if u leave it here then u will only permit to insert 1 data only
                  #! database is locked
def listbox_add_selection():
    global content
    #print(content['醫院名稱'])#? check for getting values for adding listbox selections
    my_listbox.insert(END,f"{str(idx + 1)}  {content['醫院名稱']}")
    Tk.update(root)
def retrieve_data_frm_DB_to_listbox():
    global conn
    c = conn.cursor()
    print ("Opened database successfully")
    cursor = c.execute("SELECT *  from Hospital")
    for idx, row in enumerate(cursor, 1):
        #print("---------------------------------------")
        #print(row)
        ## ('臺東縣', '台灣基督長老教會馬偕醫療財團法人台東馬偕紀念醫院', '1', '醫院評鑑合格（區域醫院）', '醫師及醫事人員類教學醫院評鑑合格', '109/1/1-112/12/31', '109/1/1-112/12/31', '089-310150', '臺東縣臺東市長沙街303巷1號')
               #0                     1                               2               3                          4                            5                  6                 7                 8                                                                                                        
        my_listbox.insert(END,f"{str(idx)} {row[0]} {row[2]} {row[1]} {row[7]} {row[8]}")
        Tk.update(root)


def get_JSON_frm_internet():
    global content,idx
    #?とりあえず例として、どこかのWeb APIを叩くことにする
    url = URL_entry.get()
    #?requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存
    response = requests.get(url)
    #?response.json()でJSONデータに変換して変数へ保存 
    #! .jason() shall do some research!!! this info might be wrong
    jsonData = response.json()
    #print(isinstance(jsonData,dict))
    #* False!! jsonData is not dict
    #?このJSONオブジェクトは、連想配列（Dict）っぽい感じのようなので
    #?JSONでの名前を指定することで情報がとってこれる
    #print(jsonData)
    #print(type(jsonData))
    #* jsonData is <class 'list'>
    for idx , content in enumerate(jsonData,0): 
        #print(content)
        listbox_add_selection()
        ##{'所在縣市': '澎湖縣', '醫院名稱': '三軍總醫院澎湖分院附設民眾診療服務處', '編號': '1', '醫院評鑑評鑑結果': '醫院評鑑合格（地區醫院）', '教學醫院評鑑結果': '醫師及醫事人員類教學醫院評鑑合格', '醫院評鑑合格效期': '106/1/1-109/12/31', '教學醫院合格效期': '106/1/1-109/12/31', '醫院電話': '06-9211116', '地址': '澎湖縣馬公市前寮里90號1-5樓'}  
        #print("====================")
        #print("idx={0}, content={1} \n".format(idx, content))
        #print(isinstance(content,dict)) #* content is type Dict
        content_values = content.values() #? 讀取dict的values
        ## dict_values(['澎湖縣', '三軍總醫院澎湖分院附設民眾診療服務處', '1', '醫院評鑑合格（地區醫院）', '醫師及醫事人員類教學醫院評鑑合格', '106/1/1-109/12/31', '106/1/1-109/12/31', '06-9211116', '澎湖縣馬公市前寮里90號1-5樓'])
        #print(idx,content_values) #? check total number of datas
        ## 122 dict_values(['澎湖縣', '三軍總醫院澎湖分院附設民眾診療服務處', '1', '醫院評鑑合格（地區醫院）', '醫師及醫事人員類教學醫院評鑑合格', '106/1/1-109/12/31', '106/1/1-109/12/31', '06-9211116', '澎湖縣馬公市前寮里90號1-5樓'])
        #print(type(content_values))
        ## <class 'dict_values'>

        
        sql_command = " insert into Hospital (City, Hospital, H_Id, Eval_Reault_Local, Eval_Reault_Teaching, Date_Valid_Local, Date_Valid_Teaching, Tel, Address) values("
        for value in content_values:
            #if isinstance(value,str) != True:             #* double checking all value are STRING
            #    print("error")
            #print(value)
            ### 澎湖縣
            ### 三軍總醫院澎湖分院附設民眾診療服務處
            ### 1
            ### 醫院評鑑合格（地區醫院）
            ### 醫師及醫事人員類教學醫院評鑑合格
            ### 106/1/1-109/12/31
            ### 106/1/1-109/12/31
            ### 06-9211116
            ### 澎湖縣馬公市前寮里90號1-5樓
            sql_command = sql_command + f'"{value}",'
        sql_command = sql_command[0:-1] + ")"  
        execute_SQL_command(sql_command)
    retrieve_data_frm_DB_to_listbox()
    conn.close()

    


get_JSON_frm_internet_btn = Button(root,command=get_JSON_frm_internet,width=15,text="GET & SAVE to DB",bg="#353130",fg="white")
get_JSON_frm_internet_btn.config(height=1)
get_JSON_frm_internet_btn.grid(row=1,column=2)




#add Frame
my_frame = Frame(root)
my_frame.grid(row=2,column=0,columnspan=2,sticky=W+E)

#scroll bar
scroll_bar_4_my_listbox = Scrollbar(my_frame,orient=VERTICAL)
scroll_bar_4_my_listbox.grid(row=2,column=1,sticky=N+S+W)

#Listbox
#*  SELECT MODE = SINGLE IS AT DEFAULT
my_listbox = Listbox(my_frame, width=110, bg="#353130",fg="white")  #?yscrollcommand -> is for horizontal scrollbar
my_listbox.grid(row=2,column=0,sticky=W+E)

scroll_bar_4_my_listbox.config(command=my_listbox.yview)


root.mainloop()



        


