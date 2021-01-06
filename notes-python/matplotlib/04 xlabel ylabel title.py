import matplotlib.pyplot as mp
import numpy as np

def mysin(data):
    mp.plot(data, np.sin(data),".--r")
    mp.xlabel("X")                  #x Label
    mp.ylabel("sin(X)")             #y label
    mp.title("sin(-10)..sim(10)")   ##TITLE
    mp.show()

#case4:using linespace
data3 = np.linspace(-10,10, 50) #產生50個項目
mysin(data3)
