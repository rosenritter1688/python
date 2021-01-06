import matplotlib.pyplot as mp
import numpy as np

def showLegned(data1,data2):
    mp.plot(data1, np.sin(data1), "x-r", label="data1")
    mp.plot(data2, np.sin(data2), "x--b", label="data2")
    mp.legend()
    mp.show()
#show legend
data2 = list(range(1,101,5))
data1 = list(range(1,101,7))
showLegned(data1, data2) 
