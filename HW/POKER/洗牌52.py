

#TODO 1.img file name needed to add 0 exp. C01.png,C02.png,C03.png
#TODO so sorted() can be used
import random
from tkinter import Tk,Label,Button,PhotoImage
from PIL import ImageTk,Image      ##縮小照片用的
from tkinter import font as tkFont  #變更字體大小用的


win = Tk()
win.title("poker")
win.geometry("1920x1080")                  #Width x Height
win.resizable(1,1)                       #1:True 0:False  此例 寬不可調, 高可調
#win.maxsize(width=1024, height=768)      #可調整最大尺寸
#win.minsize(width=100, height=100)       #可調整最小尺寸
#win.iconbitmap("C:\\Users\\clark\\Downloads\\cat.ico") #左上角的ico
win.config(bg="grey")                    #背景
win.attributes("-alpha",1)               #透明度:0(全透)到1(不透)之間 
win.attributes("-topmost",True)          #出現在螢幕最上面

helv36 = tkFont.Font(family='Helvetica', size=16, weight=tkFont.BOLD)  ##SAMPLE btn1 = Button(text='btn1', font=helv36)
#cards=set()
#
typeList=["D","S","C","H"]
num= random.randint(1,13)
cards = set()
def shuffle():
    global cards
    while len(cards) != 52:
        cardtype= random.choice(typeList)
        num = random.randint(1,13)
        str_num = str(num).strip()
        cards.add(cardtype.strip()+str_num)
shuffle()
print("set - card = ")
print(cards)
print("number of cards " + str(len(cards))) #! 52
list(cards)
print(type(cards)) #<class 'set'>
                   #! 上面轉成list 還是 set!!!!!!!! 要找以前做的資料!!!!!!!
#print(cards.pop()) #! 注意不像list pop()是刪除掉最後一個，set的pop()是random刪除掉一個
#---LABEL--for card cover---
#WIN 10
#image_cover = Image.open('/Users/bruceashbee/Documents/img/poker圖檔/poker_cover.png')
#MAC OS                   
image_cover = Image.open('/Users/bruceashbee/Documents/Python/img/poker圖檔/poker_cover.png')
#                                (height, width)
image_cover = image_cover.resize((210, 260), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image_cover)
poker_cover_label = Label(win, text="poker cover", bg="green",image=my_img)
poker_cover_label.place(x=500, y=200)



#--Label-for group 1 on the left-
Label_for_group1 = Label(win, text="cards for group 1",bg="grey")
Label_for_group1.place(x=250, y=200)#ipadx=100  -> width
#--Label-for group 2 on the right-
Label_for_group2 = Label(win, text="cards for group 2",bg="grey")
Label_for_group2.place(x=850, y=200)#ipadx=100  -> width      


def calling_left():#for group 1
    group1 = list()
    #group2 = list()
    global card_img#<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!重要不打的話會沒圖片   外面不宣告也沒關係   如果不宣告global def 一關掉資料會變洗掉
    global cards
    x_pos=250; y_pos=200
    if len(group1) < 5:
        file_name = cards.pop()
        print (file_name)
        #WIN 10
        #card_img = PhotoImage(file=f'C:\\Users\\Bruce Ashbee\Documents\\Python 2020\\img\\poker圖檔\\{file_name.strip()}.PNG')
        #MAC OS                      
        card_img = PhotoImage(file=f'/Users/bruceashbee/Documents/Python/img/poker圖檔/{file_name.strip()}.PNG')
        #img/poker圖檔/H8.PNG
        Label_for_group1 = Label(win,text='card_image',image=card_img)
        x_pos+=10
        Label_for_group1.place(x=x_pos,y=y_pos)
        Tk.update(win)       
        group1.append(Label_for_group1)
    else:
        print("cant call any more")
def calling_right():
    global cards
    pass 
    

#---calling BUTTON----
#for group 1 on the left
call_button_g1 = Button(text='start', bg='green', font=helv36,command=calling_left)
call_button_g1.place(x=250, y=160)
#for group 2 on the right
call_button_g2 = Button(text='start', bg='green', font=helv36,command=calling_right)
call_button_g2.place(x=850, y=160)






win.mainloop()  #主視窗一直循環被執行(常駐)   #一定要在最下面
