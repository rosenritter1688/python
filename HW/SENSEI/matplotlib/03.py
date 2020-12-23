import matplotlib.pyplot as mp
import numpy as np

def mysin(data):
    mp.plot(np.sin(data),".--b")
#. . . . . . . .

#case4:using linespace

data3 = np.linspace(-10,10, 50) #產生50個項目
mysin(data3)
mp.plot(data3, np.sin(data3),".--r")