from tkinter import Listbox,END,Button,ANCHOR,Label,Frame,Scrollbar,VERTICAL,RIGHT,Y,Tk,BROWSE
import tkinter as tk
root = tk.Tk()
root.geometry("600x640")
root.config(bg="#353130")
#! selcet mode CHECK LINE 20   21
#! BORWSE is for moving options around but its not working need some insearch

# Create Frame
my_frame = Frame(root)
my_frame.pack()



#scroll bar
scroll_bar_4_my_listbox = Scrollbar(my_frame,orient=VERTICAL)
scroll_bar_4_my_listbox.pack(side=RIGHT,fill=Y) #? y is to fill UP and DOWN all the way 
                             #? pack in on RIGHT hand side
#Listbox
#*  SELECT MODE = SINGLE IS AT DEFAULT.  <OTHER OPTIONS> BROWSE, MULTIPLE, EXTENDED 
my_listbox = Listbox(my_frame, width=50, bg="#353130",fg="white", yscrollcommand=scroll_bar_4_my_listbox.set, selectmode = BROWSE)  #?yscrollcommand -> is for horizontal scrollbar
my_listbox.pack(pady=15)

## coz of my_listbox no defined so got to put it here

scroll_bar_4_my_listbox.config(command=my_listbox.yview)


# my_listbox.insert(0, "This is an item")   #? 0 -> put it in the first one
#                                           #? END -> put it  in the END

my_listbox.insert(END, "This is an item")
my_listbox.insert(END, "second item")


my_list = ["1","2","3","4","2","3","4","2","3","4","2","3","4","2","3","4","2","3","4","2","3","4","2","3","4"]

for content in my_list:
    my_listbox.insert(END,content)


my_listbox.insert(3, "this is an new item") #? put it in the 4th place

def delete_all():
    my_listbox.delete(0,END) #? delete all

def delete():
    my_listbox.delete(ANCHOR)  #? when something in the list box is highlighted when you click on it, That is the ANCHOR
    Tk.update(root)

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

global my_label

delete_all_button = Button(root, height=1, width=10,bg="#353130",fg="white", text="delete_all",command=delete_all)
delete_all_button.pack(pady=15)

my_button = Button(root, height=1, width=10,bg="#353130",fg="white", text="DELETE",command=delete)
my_button.pack(pady=15)

select_button = Button(root, height=1, width=10,bg="#353130",fg="white", text="SELECT",command=select)
select_button.pack(pady=15)

my_label = Label(root, height=1, width=10,bg="#353130",fg="white", text="my_label")
my_label.pack(pady=15)
root.mainloop()