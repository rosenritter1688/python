# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:44:17 2020

@author: Administrator
"""

'''
DEF practice 1
...
n = int(input("pls enter a 1st number"))
x = int(input("pls enter a 2nd number"))
z = int(input("pls enter a 3rd number"))

def getMax(): 
    global n
    global x
    global z
    if (n > x and n > z):
        return n
    elif (x > n and x >z):
        return x
    else:
        return z
    
ans = getMax()
print(ans)

'''

a = 1234567
b = "1234567"
def setComma():
    print("{0:,}".format(int(a)))
    print("{0:,}".format(int(b)))
  
setComma()
    


