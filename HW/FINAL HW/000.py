import pandas as pd
import matplotlib.pyplot as plt
listx = []
listy =[]
x = 0.1 #x3 - 2x2 + 2x 
def getY(x):
    return x*x*x - 2*x*x + 2*x
for idx in range(1,1000):
    listx.append(x)
    listy.append(getY(x))

dataframe1 = pd.DataFrame({'x':listx,'y':listy})
dataframe1.plot(kind='bar')
plt.show()