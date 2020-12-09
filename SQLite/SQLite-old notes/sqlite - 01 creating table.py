# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:12:15 2019

@author: Bruce
"""

"""--------------------
創建表
--------------------"""



import sqlite3                       
conn = sqlite3.connect('C:\\Users\\Bruce Ashbee\\Documents\\Python\\SQLite\\SQLite-old notes\\test.db')          

'''
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
Open database successfully
'''

print ("Opened database successfully")

'''-------------2
making code shorter w a variable called c

c = conn.cursor()
c.execute("CREATE TABLE COMPANY         ----->" change to ' x 3 times
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL")             ----->" change to ' x 3 times

---------------2'''


conn.cursor().execute('''CREATE TABLE if not exists COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);''')

#if not exist加進去後
#如果已經有student TABLE了他就不會加
#也不會出現錯誤訊號
###  OperationalError: table student already exists



print ("Table created successfully")
conn.commit()  #將之前的操作變更至資料庫中
conn.close()   #關閉資料庫連線


# if run this at the second times will show
# OperationalError: table COMPANY already exists