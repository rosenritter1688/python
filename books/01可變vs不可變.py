
#* 可變與不可變
a = 3
a = 4
print(a)
## 4


#* LIST是可變

name = 'Frank'
height = 177
weight = 68
title = 'software Engineer'
languages =["C","Python"]
LIST_01 = [name,height,weight,title,languages]
LIST_01[2] = 75 #! get fat

print(LIST_01)
##['Frank', 177, 75, 'software Engineer', ['C', 'Python']]


#* 別名alias
#* 不可變 int float string
#* 可變 list
#! EXAMPLE 01 - int
a = 3
b = a
print("a = " + str(a) + ", b = " +  str(b))
## a = 3, b = 3

b = 4 #! <<<<
print("a = " + str(a) + ", b = " +  str(b))
## a = 3, b = 4

"""
a = 4 #! <<<<
print("a = " + str(a) + ", b = " +  str(b))
## a = 4, b = 3
"""
#! example 01 coz int 不可變所以沒改到b look example 2 for different


#! example 02  - list
a = [60,71,82]
b = a
print("a = "+str(a) + ", b = "+str(b))
## a = [60, 71, 82], b = [60, 71, 82]
b[0] = 99 
print("a = "+str(a) + ", b = "+str(b))
## a = [99, 71, 82], b = [99, 71, 82]
#! example 02 是list  是可變的所以改了b連a都會一起改
"""
a[0] = 99 
print("a = "+str(a) + ", b = "+str(b))
## a = [99, 71, 82], b = [99, 71, 82]
"""