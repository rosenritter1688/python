from tkinter import * #Listbox,END,Button,ANCHOR,Label,Frame,Scrollbar,VERTICAL,RIGHT,Y,Tk,MULTIPLE,Entry
import tkinter as tk

main = tk.Tk()
main.geometry("1000x940")                  #Width x Height
main.config(bg="#353130")                  #背景
main.title("FINAL HW")              
main.resizable(1,1)                        #1:True 0:False  此例 寬不可調, 高可調
main.maxsize(width=1500, height=1080)      #可調整最大尺寸
#main.minsize(width=800, height=640)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico                 
main.attributes("-alpha",1)                #透明度:0(全透)到1(不透)之間 
main.attributes("-topmost",True)           #出現在螢幕最上面

def call_water_read():
    import water_read

#? Bttn1
call_water_read_btn = Button(main,command=call_water_read,width=15,text="GET from URL",bg="#353130",fg="white")
call_water_read_btn.grid(row=1,column=0,columnspan=2,sticky="WE")

# #? Bttn2
# insert_to_DB_btn = Button(main,command=insert_to_DB,width=15,text="將選擇的項目存到資料庫,可只選像要存的",bg="#353130",fg="white")
# insert_to_DB_btn.grid(row=3,column=0,columnspan=2,sticky="WE")

main.mainloop()
