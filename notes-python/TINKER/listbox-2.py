from tkinter import *
from tkinter import ttk

def show_selection():
    for i in lb.curselection():
        print(lb.get(i))


if __name__ == '__main__':
    root = Tk()
    root.title('Listbox 1')

    # フレーム
    frame = ttk.Frame(root, padding=400)
    frame.grid()

    # リストボックス
    currencies = ['JPY', 'USD']
    v = StringVar(value=currencies)
    lb = Listbox(
        frame, listvariable=v,   #! 
        selectmode='multiple', height=4)
    lb.insert(END, 'EUR')
    lb.bind(
        '<<ListboxSelect>>',
        lambda e: show_selection())
    lb.grid(row=0, column=0)

    # Button
    button1 = ttk.Button(
        frame, text='OK',
        command=lambda: show_selection())
    button1.grid(row=0, column=1)

    root.mainloop()