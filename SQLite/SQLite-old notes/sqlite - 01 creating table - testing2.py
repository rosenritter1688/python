# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:46:32 2019

@author: Bruce
"""
import sqlite3                       
#conn = sqlite3.connect('test-1.db')   #  short form for --->line 14,58,60





#conn.cursor().execute('CREATE TABLE if not exists student
#           (std_id	TEXT,
#            std_name	TEXT,
#            sex	TEXT,
#        PRIMARY KEY(std_id));')


### SyntaxError: EOL while scanning string literal
# '  -->   '''
'''
setting varible data_table_student
as
CREATING TABLE student coding

'''
data_table_student = ('''CREATE TABLE if not exists student
           (std_id	TEXT,
            std_name	TEXT,
            sex	TEXT,
        PRIMARY KEY(std_id));''')
# set std_id as PK


'''
創一個student TABLE到test-2.db
'''


sqlite3.connect('test.db').cursor().execute(data_table_student)


#if not exist加進去後
#如果已經有student TABLE了他就不會加
#也不會出現錯誤訊號
###  OperationalError: table student already exists


'''
sqlite3.connect('test-2.db')

連接到一個現有的數據庫。如果數據庫不存在，那麼它就會被創建，最後將返回一個數據庫對象。
在這裡，您也可以把數據庫名稱複製為特定的名稱 :memory:，這樣就會在 RAM 中創建一個數據庫。
現在，讓我們來運行上面的程序，在當前目錄中創建我們的數據庫 test.db。您可以根據需要改變路徑。
保存上面代碼到 sqlite.py 文件中，並按如下所示執行

--1-----------------------------------------
EXP:
conn = sqlite3.connect(:memory:)
--1----------------------------------
。如果數據庫成功創建，那麼會顯示下面所示的消息：

$chmod +x sqlite.py
$./sqlite.py

'''


'''
CREATE TABLE if not exists student
'''


    
print ("Table student created successfully")
sqlite3.connect('test.db').commit()  #將之前的操作變更至資料庫中
#conn.commit()  
sqlite3.connect('test.db').close()   #關閉資料庫連線
#conn.close()  