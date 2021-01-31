from tkinter import Tk,Button
import tkinter as tk
root = tk.Tk()
root.geometry("600x640")
root.config(bg="#353130")

def getTextInput():
    result=textbox_example.get("1.0","end")#?retrive text from textbox and name content as result
    #textbox_example.delete("1.0","end")   #?delete text in the textbox_example 
    print(result)
    textbox_show.delete("1.0","end")       #? delete text in textbox_show first
    textbox_show.insert(1.0,result)        #? pass data to textbox 



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