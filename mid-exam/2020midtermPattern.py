# -*- coding: utf-8 -*-
"""
期中考:2020-11-11
"""
import random
from tkinter import *
win = Tk()
win.geometry("1000x500")
win.config(bg='lightgreen')



#-----------------------------------------------------
typeList=["D","S","C","H"]
num= random.randint(1,13)
cards = set()

while len(cards) != 52:
    cardtype= random.choice(typeList)
    num = random.randint(1,13)
    str_num = str(num).strip()
    cards.add(cardtype.strip()+str_num)
    #result.insert(END, f"{cards}\n")
    #Tk.update(win)
print("numbers in card ",len(cards))
def shuffle():
    #result.delete(0,END)  
    global cards
    num_cards = 0
    while len(cards) > 0:
        num_cards += 1
        x = cards.pop()
        result.insert(END, f"{num_cards} : {x}\n")
        #Tk.update(win)


displayShuffle = Button(win, text='(1)顯示洗牌結果',command=shuffle)
displayShuffle.grid(row=0, column=0, sticky=W)


#text box
result = Text(win, width=20, height=20)
result.grid(row=1, column=0,  columnspan=3, sticky=E+W)
scroll1 = Scrollbar(win, command=result.yview)
scroll1.grid(row=1, column=3, sticky=N+S)

#-------------------------------------------------------

displayQueue = Button(win, text='(2)顯示2入5出排隊結果')
displayQueue.grid(row=0, column=1, sticky=W)
#-----------------------------------------------------
'''
3.40%讀取成績檔record.txt, 內容格式為: “學號,科目,成績”, 
若科目為MATH, 90分以下(不含90分), 就加10分, 其他科目成績照舊, 結果如下
'''

data_list=list()


def result_adjustment():
    result.delete('1.0', END)
    with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\mid-exam\\record.txt',"r+") as f:
        for a in f:
            x = a.split(",")
            print("x = ",x)
            data_list.append(x)
            print("dat_list = ",data_list)

    for id,subject,marks in data_list:
        '''
        print("id = {}".format(id))
        print("subject = {}".format(subject))
        print("marks = {}".format(marks))
        '''
        if int(marks) < 90:
            changed_marks = int(marks) + 10
            result.insert(END, "學號 : {}, 科目 : {}, 分數 : {} \n".format(id,subject,str(changed_marks)))
            Tk.update(win)
        else:
            result.insert(END, "學號 : {}, 科目 : {}, 分數 : {} \n".format(id,subject,str(marks)))
            Tk.update(win)
        



readFile = Button(win, text='(3讀取成績檔)', command = result_adjustment)
readFile.grid(row=0, column=2, sticky=W)

win.mainloop()