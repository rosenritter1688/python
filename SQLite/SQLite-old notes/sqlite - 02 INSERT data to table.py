# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:33:10 2019

@author: Bruce
"""

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''
             INSERT INTO COMPANY 
             (ID,
             NAME,
             AGE,
             ADDRESS,
             SALARY)
             
      VALUES (1, 'Paul', 32, 'California', 20000.00 )''');
conn.execute('''INSERT INTO COMPANY 
             (ID,
             NAME,
             AGE,
             ADDRESS,
             SALARY)
      VALUES (2,'Allen', 25, 'Texas', 15000.00 )''');

conn.execute('''INSERT INTO COMPANY 
             (ID,
             NAME,
             AGE,
             ADDRESS,
             SALARY)
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )''');

conn.execute('''INSERT INTO COMPANY 
             (ID,
             NAME,
             AGE,
             ADDRESS,
             SALARY)
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )''');

conn.commit() #將之前的操作變更至資料庫中
print ("Records created successfully")
conn.close()  #關閉資料庫連線