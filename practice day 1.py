# -*- coding: Big5 -*-
import locale#模組把千分位的區分,拿掉 #! but will turn to float too
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 
#! 只可以把string的逗點拿掉, int or float cant use this mater


A = '111,111.222'
print(type(A))
## <class 'str'>  
print("1 -> ",locale.atof(A))
##111111.222
x = locale.atof(A)
print("1-2 > ",type(x))
##1-2 >  <class 'float'>  #! string will turn to float
print("2 -> ",type(locale.atof(A)))
##<class 'float'>


print(locale.atof('111,111'))
#111111.0
# input1 = int(input("pleae input 7,000,000 for N1 : "))
# input2 = float(input("pleae input 100.006 for N2 : "))
# input3 = float(input("pleae input 20.016 for N3 : "))
input1 = 7_000_000
input2 = 100.006
input3 = 20.016

print("N1 : {0:,}".format(input1))
print("N2 : {0}".format(input2))
print("N3 : {0}".format(input3))
changedInput1 = ("{0:10,.2f}".format(float(input1)))
changedInput2 = ("{0:12,.2f}".format(float(input2)))
changedInput3 = ("{0:12,.2f}".format(float(input3)))
print("type of changedInput3 = ",type(changedInput3))
print("--checking changed values --")
print("changedInput1 = " + changedInput1)
print("changedInput2 = " + changedInput2)
print("changedInput3 = " + changedInput3)
print(changedInput1+changedInput2+changedInput3)#只會把字串加再一起





sum = locale.atof(changedInput1) + float(changedInput2) + float(changedInput3)
print(sum)

#N1C = ("{0:,}".format(input1))
#ChangedInput2 = ("{0}"
#print("N1 + N2 + N3 等於 {0} + {1} + {2} ".format(changedInput1,changedInput2,changedInput3) + "= " + (changedInput3 + changedInput2 + changedInput1)


XZ = "123,456.789"
XZ.replace(',','')  #! wrong way to using this 
print(XZ)
##123,456.789 
ui=XZ.replace(',','')
print(ui)
#123456.789

s = 'one two one two one'
ji = s.replace(',', '')
print(ji)
#123456.789

