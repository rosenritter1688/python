# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:47:48 2020

@author: Administrator
"""

nameUser = input("pleae enter ur name : ")
height = float(input("pls enter your height in cm "))
weight = float(input("pls enter your weight in KG "))
height2 = height/100
bmi2 = float(weight)/((float(height2)*float(height2)))

print("{0} your BMI is {1:10.2f}".format(nameUser,bmi2))

print("{0} your BMI is {1}".format(nameUser,weight))
