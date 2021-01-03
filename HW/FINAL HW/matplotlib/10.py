import numpy as np
import matplotlib.pyplot as plt

'''linspace
start, stop, numの3つです。

startは数列の開始点を指定する
stopは数列の終了点を指定する
numは数列の要素の数を指定する
'''
x_1 = np.linspace(0, 1, 100)
y_1 = x_1
x_2 = np.linspace(0, 1, 100)
y_2 = x_2 ** 2
x_3 = np.linspace(0, 1, 100)
y_3 = x_3 ** 3
x_4 = np.linspace(0, 1, 100)
y_4 = x_4 ** 4
fig = plt.figure()

ax_1 = fig.add_subplot(221)   #? 2 x 2 so 4 charts first chart
ax_2 = fig.add_subplot(222)
ax_3 = fig.add_subplot(223)
ax_4 = fig.add_subplot(224)

ax_1.plot(x_1, y_1)
ax_2.plot(x_2, y_2)
ax_3.plot(x_3, y_3)
ax_4.plot(x_4, y_4)

plt.show()

print(np.linsapce(0 ,30, 11))