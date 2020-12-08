# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:55:54 2019

@author: Bruce


只有刪除ID2的資料

"""

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("Opened database successfully")

'''
LINE 23
c.execute("DELETE from COMPANY where ID=2;")
只有刪除ID2的資料
'''
#c.execute("DELETE from COMPANY where ID=2;")
''' 刪除全部資料    '''
c.execute("DELETE from COMPANY")


conn.commit()#將之前的操作變更至資料庫中
print ("Total number of rows deleted :", conn.total_changes)
                                            #.total_changes()
                                            #該例程返回自數據庫連接打開以來被修改、插入或刪除的數據庫總行數。
#c.execute("DELETE from COMPANY")  LINE 25
#刪除全部資料
###Total number of rows deleted : 3


'''
顯示被刪除後剩下的資料
'''
cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

   


print ("Operation done successfully")
conn.close() #關閉資料庫連線

###Opened database successfully
###Total number of rows deleted : 1
###ID =  1
###NAME =  Paul
###ADDRESS =  California
###SALARY =  20000.0 

###ID =  3
###NAME =  Teddy
###ADDRESS =  Norway
###SALARY =  20000.0 

###ID =  4
###NAME =  Mark
###ADDRESS =  Rich-Mond 
###SALARY =  65000.0 

###Operation done successfully