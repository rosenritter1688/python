import matplotlib.pyplot as mp
def easyPlot(data):
     mp.plot(data, "-.r")     #設定折線規格
     mp.show()
# case 1
data = [100,200,150, 300, 250, 600]    
easyPlot(data)



##參數1
#x  X
#. 小圓點
#o 大圓點
#s 正方形
#,  好像沒有

##參數2
#- 實線
#--虛線
#. 點虛線
#-. 虛線和點

##參數3
#color
#b blue
#g green
#r red
#c cyan青色
#m magenta 微紫色
#y yellow
#k black
#w while