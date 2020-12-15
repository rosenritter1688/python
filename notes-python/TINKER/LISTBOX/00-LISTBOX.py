from tkinter import Listbox,END
import tkinter as tk
root = tk.Tk()
root.geometry("600x640")
root.config(bg="#353130")
#* List Box
my_listbox = Listbox(root)
my_listbox.pack(pady=15)


# my_listbox.insert(0, "This is an item")   #? 0 -> put it in the first one
#                                           #? END -> put it  in the END

my_listbox.insert(END, "This is an item")
my_listbox.insert(END, "second item")


my_list = ["1","2","3","4"]

for select in my_list:
    my_listbox.insert(END,select)


my_listbox.insert(3, "this is an new item") #? put it in the forth place

# textbox_example=tk.Text(root, height=10,width=30,bg="#353130",fg="white")
# textbox_example.grid(row=0,column=0)

# scrollbar_4_textbox_example = tk.Scrollbar(root)
# scrollbar_4_textbox_example.grid(row=0, column=1, sticky="NS")

# btnRead=tk.Button(root, height=1, width=10,bg="#353130",fg="black", text="Read",command=getTextInput)
# btnRead.grid(row=1,column=0,sticky="WE",columnspan=2)

# textbox_show=tk.Text(root, height=10,width=30,bg="#353130",fg="white")
# textbox_show.grid(row=2,column=0)

# scrollbar_4_textbox_show = tk.Scrollbar(root)
# scrollbar_4_textbox_show.grid(row=2, column=1, sticky="NS")

root.mainloop()