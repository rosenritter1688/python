# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:42:03 2019

@author: Bruce

https://www.runoob.com/sqlite/sqlite-python.html
"""

'''
UPDATE 操作

下面的 Python 代碼顯示了如何使用 UPDATE 語句來更新任何記錄，
然後從 COMPANY 表中獲取並顯示更新的記錄：
'''


import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("Opened database successfully")

c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")

# 修正表格ｃｏｍａｐｎｙ裡面的ＩＤ　１的SALARY
#　變更為２５０００

conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()


###Opened database successfully
###Total number of rows updated : 1
###ID =  1
###NAME =  Paul
###ADDRESS =  California
###SALARY =  25000.0 

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