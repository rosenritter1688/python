import matplotlib.pyplot as mp
import numpy as np
data = list(range(1,101,3)) #3的倍數
data2 = list(range(1,101,5))
data3 = list(range(1,101,7))
def showLegned(data1,data2,data3):
    mp.plot(data, "x-r", label="data1")
    mp.plot(data2, "o--b", label="data2")
    mp.plot(data3, "s--c", label="data3")
    mp.legend()
    mp.show()

showLegned(data, data2,data3) 
