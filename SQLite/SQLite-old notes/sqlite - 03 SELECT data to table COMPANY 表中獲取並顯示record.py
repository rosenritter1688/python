# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:34:06 2019

@author: Bruce
"""
'''
SELECT 操作

下面的 Python 程序顯示了如何從前面創建的 COMPANY 表中獲取並顯示記錄：
'''
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("Opened database successfully")

cursor = c.execute("SELECT id, name, address, salary  from COMPANY")

#SELECT   COMPANY 表中獲取並顯示記錄：

for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close() #關閉資料庫連線

###Opened database successfully
###ID =  1
###NAME =  Paul
###ADDRESS =  California
###SALARY =  20000.0

###ID =  2
###NAME =  Allen
###ADDRESS =  Texas
###SALARY =  15000.0

###ID =  3
###NAME =  Teddy
###ADDRESS =  Norway
###SALARY =  20000.0

###ID =  4
###NAME =  Mark
###ADDRESS =  Rich-Mond
###SALARY =  65000.0

###Operation done successfully
###