from tkinter import Tk,Scale,Scrollbar,Text,END
win=Tk()
win.geometry("1900x900")
win.config(bg='grey')
#-------------------------

def calculate(self):
    result.delete('1.0', END)
    result2.delete('1.0', END)
    result3.delete('1.0', END)
    value_1 = int(scale.get())
    #s = value_1 + 1
    for i in range (1,value_1 + 1):
        if i % 2 == 0:
            print(i)
            result.insert(END, f"{i:5} \n") 
        elif i % 3 == 0:
            result2.insert(END, f"{i:5} \n")
        elif i % 5 == 0:
            result3.insert(END, f"{i:5} \n")
scale = Scale(win, from_ = 1, to_ = 100,showvalue=1,command=calculate)
scale.grid(row=0, column=0, sticky = "NS")
#----------------------
result = Text(win)#雙數用
result.grid(row=0, column=1)
#-----------------------
scroll = Scrollbar(win)
scroll.grid(row=0, column=2, sticky = "NS")
#------------------------
result2 = Text(win)#3的倍數用
result2.grid(row=0, column=3)
#-----------------------
scroll2 = Scrollbar(win)
scroll2.grid(row=0, column=4, sticky = "NS")

result3 = Text(win)#5的倍數用
result3.grid(row=0, column=5)
#-----------------------
scroll3 = Scrollbar(win)
scroll3.grid(row=0, column=6, sticky = "NS")
win.mainloop()
