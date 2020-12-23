import matplotlib.pyplot as mp
import numpy as np

def mysin(data):
    mp.plot(data, np.sin(data),".--r")
    mp.xlabel("X")
    mp.ylabel("sin(X)")
    mp.title("sin(-10)..sim(10)")   
    mp.show()

#case4:using linespace
data3 = np.linspace(-10,10, 50)
mysin(data3)
