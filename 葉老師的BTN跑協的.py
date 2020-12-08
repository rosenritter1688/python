

from tkinter import Button,Tk,Label,PhotoImage
#import PIL
import time
win=Tk()
win.geometry("800x800")
xpos = 0.1
ypos=0.1
doTick = True
def startticker():
       global doTick
       tickJob()
def tickJob():
   global xpos, ypos, doTick
   #if not doTick: #! same as below
   if doTick != True:
      return
   myTime = time.time()  # 1564734019.2818341
   timeX = time.localtime(myTime) #time.struct_time(tm_year=2019, tm_mon=8, tm_mday=2, tm_hour=16, tm_min=20, tm_sec=19, tm_wday=4, tm_yday=214, tm_isdst=0)
   myLabel.config(text=str(time.asctime(timeX)))  # Fri Aug  2 16:22:40 2019
   btn.place_configure(relx=xpos, rely=ypos)
   if(xpos <= 0.9):
      xpos += 0.1; ypos += 0.1
   else:
      xpos = 0.1; ypos = 0.1
   win.after(1000,tickJob) # tickJob不能帶參數, 所以帶參數要用lambda
def stopTick():
    global doTick
    doTick = False
#===== program begin =====
#win 10
##img = PhotoImage(file='C:\\Users\Bruce Ashbee\\Documents\\traffic-lights-green.PNG')
#MAC
img = PhotoImage(file='//Users//bruceashbee//Documents//img//交通工具//traffic-lights-green.PNG')
btn = Button()
btn.config(image=img)
btn.place(x=1, y=1,anchor='center') #圖形中心點在mouse點到的位置

btnstart = Button(text="Start", command=startticker)
btnstart.config(command=startticker)
btnstart.place(x=200, y=200,anchor='center') #圖形中心點在mouse點到的位置
btnstop = Button(text="Stop")
btnstop.config(command=stopTick)
btnstop.place(x=200, y=250,anchor='center') #圖形中心點在mouse點到的位置
myLabel = Label()
myLabel.pack()



win.mainloop()
