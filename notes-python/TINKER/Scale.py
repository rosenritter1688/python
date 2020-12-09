from tkinter import *
'''
win = Tk()
win.geometry("400x400")
win.title("Test Scale")
win.config(bg="skyblue")
def getValue(self):
    myLabel.config(text=int(myScale.get()))
#scale
myScale = Scale()
myScale.config(label="指標",length=200, from_=0, to_=1000, orient=VERTICAL, command=getValue)
myScale.config(showvalue=1)
myScale.place(x=100, y=10)
#Label
myLabel = Label(text="指標數值", fg="red")
myLabel.place(x=50, y=100)
win.mainloop()

'''
master = Tk()

leftValue = IntVar()  # IntVars to hold
rightValue = IntVar() # values of scales

leftScale = Scale(master, from_=0, to=249, variable=leftValue, showvalue=0)
leftScale.set(152)

rightScale = Scale(master, from_=0, to=249, variable=rightValue, showvalue=0)
rightScale.set(152)

leftLabel = Label(master, textvariable=leftValue)   # labels that will update
rightLabel = Label(master, textvariable=rightValue) # with IntVars as slider moves

leftLabel.grid(row=0, column=0)
leftScale.grid(row=0, column=1)
rightLabel.grid(row=0, column=3)
rightScale.grid(row=0, column=2)

mainloop()