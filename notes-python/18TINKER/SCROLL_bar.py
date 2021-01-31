
#? w = Scrollbar(master, options) 
from tkinter import *
  
root = Tk() 
root.geometry("150x200") 


##create frame
frame_4_label = Label(root)
frame_4_label.pack()

w = Label(root, text ='GeeksForGeeks', 
                         font = "50")  
w.pack() 
   
scroll_bar = Scrollbar(frame_4_label) 
scroll_bar.pack( side = RIGHT, 
                 fill = Y ) #? Y -> fill up UP and DOWN       
                     #! X is not working properly, need to do some research for horizontal scrollbar
mylist = Listbox(frame_4_label,  
                 yscrollcommand = scroll_bar.set )  #! yscrollcommand is must research needed
   
for line in range(1, 26): 
    mylist.insert(END, "Geeks " + str(line)) 
  
mylist.pack( side = LEFT, fill = BOTH ) 
  
scroll_bar.config( command = mylist.yview ) 
   
root.mainloop() 