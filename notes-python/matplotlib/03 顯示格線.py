import matplotlib.pyplot as mp
def twoline(data1, data2): # 若再加data3當然就會有第3條線,資料數可不同
    mp.plot(data1, "x-r", data2, "x--b")  
    mp.grid()   #會顯示格線
    mp.show()
data1 = [100,200,150, 300, 250, 600]    
data2 = [70, 150, 120, 320, 270, 500]
twoline(data1,data2)
