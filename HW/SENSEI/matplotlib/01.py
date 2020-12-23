import matplotlib.pyplot as mp
import matplotlib.pyplot as mp
def easyPlot(data):
    mp.plot(data)   #預設為折線圖
    mp.show()
# case 1
data = [100,200,150, 300, 250, 600]  #只給y值    
easyPlot(data)
