
#? importModule.py
# name = None
# def bmi(h,w):
#     r = w/h/h
#     return r
# bmi(170,70)

import importModule
importModule.name = "Bruce"
#! 呼叫importModule.py的variable
r = importModule.bmi(170,70)
    #! 使用importModule.py的def bmi
print(r)

## 0.002422145328719723

x = 70/170/170
print("x = ",x)