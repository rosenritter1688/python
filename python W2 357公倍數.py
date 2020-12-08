# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:38:44 2020

@author: Administrator
"""

for x in range(1,1001):
    if ( x%3 == 0 and x%5 == 0 and x%7 ==0 ):
        print("{} 是3,5,7的公倍數".format(x))
    else:
        continue
        
for x in range(1,101):
    if ( x%3 == 0 and x%5 == 0 and x%7 ==0 ):
        print("{} 是3,5,7的倍數".format(x))
    elif (x%3 == 0 and x%5 == 0):
        print("{} 是3,5的倍數".format(x))
    elif (x%3 == 0 and x%7 == 0):
        print("{} 是3,7的倍數".format(x))
    elif (x%5 == 0 and x%7 == 0):
        print("{} 是5,7的倍數".format(x))
    elif (x%3 == 0 ):
        print("{} 是3的倍數".format(x))
    elif (x%5 == 0 ):
        print("{} 是5的倍數".format(x))
    elif (x%7 == 0 ):
        print("{} 是7的倍數".format(x))
    else:
        print("{} 不是3,5,7的倍數".format(x))
        
        
        
        