from tkinter import *
import tkinter as tk
root = tk.Tk()
root.geometry("600x640")
root.config(bg="#353130")
# Drop Down Box

clicked = StringVar()
drop = OptionMenu(root, clicked, "Mon", "Tues" , "Wed" , "Thurds" , "Fri")
drop.pack()


root.mainloop()