from tkinter import Listbox,END,Button,ANCHOR,Label,Frame,Scrollbar,VERTICAL,RIGHT,Y,Tk,MULTIPLE
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
my_listbox = Listbox(my_frame, width=50, bg="#353130",fg="white", yscrollcommand=scroll_bar_4_my_listbox.set, selectmode = MULTIPLE)  #?yscrollcommand -> is for horizontal scrollbar
my_listbox.pack(pady=15)

## coz of my_listbox no defined so got to put it here

scroll_bar_4_my_listbox.config(command=my_listbox.yview)


# my_listbox.insert(0, "This is an item")   #? 0 -> put it in the first one
#                                           #? END -> put it  in the END


my_list = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven"]

for content in my_list:
    my_listbox.insert(END,content)
my_listbox.insert(15, "this is an new item") #? put it in the 16th place

def delete_all():
    my_listbox.delete(0,END) #? delete all

def delete():
    value = my_listbox.get(ANCHOR)
    my_listbox.delete(ANCHOR)  #? when something in the list box is highlighted when you click on it, That is the ANCHOR
    Tk.update(root)
    my_label.config(text=f"{value} is deleted")

def select_btn_function():
    my_label.config(text=my_listbox.get(ANCHOR))

global my_label

delete_all_button = Button(root, height=1, width=10,bg="#353130",fg="white", text="delete_all",command=delete_all)
delete_all_button.pack(pady=15)

my_button = Button(root, height=1, width=10,bg="#353130",fg="white", text="DELETE",command=delete)
my_button.pack(pady=15)

select_button = Button(root, height=1, width=10,bg="#353130",fg="white", text="SELECT",command=select_btn_function)
select_button.pack(pady=15)

def show_multiple_selected_list():
    selected_options = ""
    print(my_listbox.curselection()) #? print out the current list of selections   
    ## (5, 7, 8)  #? 第一個是0   index number of list
    for item in my_listbox.curselection():              #!   item    is for each time we loop we get the index of the list box
        selected_options = selected_options + my_listbox.get(item) + "\n"  #?my_listbox.get() -> get the index we want to get
        ## terminal (0, 1, 2) Label ( one "\n" two  "\n" three "\n"  ) #! line at 65 , label will get the text of the selected lists 
        selected_options = selected_options + str(item) + "\n"   #! label will get index number of the selected lists
        ## terminal (0, 1, 2) Label ( 0 "\n" 1  "\n" 2 "\n"  )
    my_label.config(text=selected_options)

delete_function_4_multiple_mode = Button(root, height=1, width=50,bg="#353130",fg="white", text="show_multiple_selected_list",command=show_multiple_selected_list)
delete_function_4_multiple_mode.pack(pady=15)

def delete_function_4_multiple_selections():
    """
    for item in my_listbox.curselection():
        my_listbox.delete(item) #! this is not going to work coz each time it loops and  deletes an item, the list itself changes, the list wont sync up 
    """ 
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)

delete_function_4_multiple_mode_button = Button(root, height=1, width=50,bg="#353130",fg="white", text="delete_function_4_multiple_selections",command=delete_function_4_multiple_selections)
delete_function_4_multiple_mode_button.pack(pady=15)



my_label = Label(root, height=50, width=10,bg="#353130",fg="white", text="my_label")
my_label.pack(pady=15)
root.mainloop()