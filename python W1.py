# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:57:13 2020

@author: Bruce Ashbee
"""

# for i in range(3):
#     print("x")
    
    
# a = b = c =100
# s1,s2,s3 = 100 ,200, 300

# print('s1'+s1)
# print('s2'+s2)


input1 = int(input("pleae input 7000000 for N1 : "))
input2 = float(input("pleae input 100.006 for N2 : "))
input3 = float(input("pleae input 20.016 for N3 : "))

print("check the value entered")
print("N1 : {0:,}".format(input1))
print("N2 : {0}".format(input2))
print("N3 : {0}".format(input3))
changedInput1 = ("{0:10,.2f}".format(float(input1)))
changedInput2 = ("{0:12,.2f}".format(float(input2)))
changedInput3 = ("{0:12,.2f}".format(float(input3)))
print("--changed input values check--")
print("changedInput1 = " + changedInput1)
### changedInput1 = 7,000,000.00
print("changedInput2 = " + changedInput2)
### changedInput2 =       100.01
print("changedInput3 = " + changedInput3)
### changedInput3 =        20.02


#注意
print(changedInput1+changedInput2+changedInput3)#只會把字串加再一起
###  7,000,000.00      100.01       20.02
print("sample 2")
print(str(changedInput1)+str(changedInput2)+str(changedInput3))
print("sample3")
print("abc"+"def"+"ghi")

#
#
#
#把changedInput1數字,拿掉才可以做計算(方法一)
try1 = changedInput1.replace(",", "")
print("try1 = " + try1)
print(float(try1)+float(changedInput2)+float(changedInput3))
### 7000120.029999999
print(float(changedInput1.replace("," , ""))+float(changedInput2)+float(changedInput3))
#把數字,拿掉才可以做計算(方法二)
import locale#模組把千分位的區分,拿掉
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
##example : 把數字,拿掉才可以做計算
A = '111,111.222'
print(locale.atof(A))
#111111.222
print(locale.atof('111,111'))
#111111.0

sum = locale.atof(changedInput1) + float(changedInput2) + float(changedInput3)
print(sum)

#N1C = ("{0:,}".format(input1))
#ChangedInput2 = ("{0}"
print("N1 + N2 + N3 等於 {0} + {1} + {2} ".format(changedInput1, changedInput2, changedInput3) + " = {0}".format(sum))
try2 = locale.atof(changedInput1)
print("N1 + N2 + N3 等於 {0} + {1} + {2} ".format(changedInput1, changedInput2, changedInput3) + " = " + str(float(try2) + float(changedInput2) +float(changedInput3)))

sum2=float(try2) + float(changedInput2) +float(changedInput3)
print("sum is {:10,.2f}".format(sum2))