# with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
#     lines = f.readlines() #! read all and turn it into a list


# with conn.cursor() as curs:
#     curs.execute(SQL)


#TODO 1.cursor 滑鼠浮標but better do some reaseach  https://qiita.com/knoguchi/items/3d5631505b3f08fa37cc

import sqlite3
def execSQLcommand(sqlstr):
    global connect_To_Database
    global cursor_function
    try:
        cursor_function = connect_To_Database.execute(sqlstr)
        connect_To_Database.commit()
        print("指令已成功執行:" + sqlstr)
        return cursor_function
    except:
      print("指令有誤:", sqlstr)
#-------create database or open connection -----
#設定myConn的同時建立資料庫(if not exiested), 或打開(如果已存在)
#!win 10
#connect_To_Database = sqlite3.connect("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\SQLite\\std.db")
#!mac
connect_To_Database = sqlite3.connect("//Users//bruceashbee//Documents//SQLite//std.db")
cursor_function = connect_To_Database.cursor()
#myConn = sqlite3.connect(':memory:') # Create db in memory

#select data
sqlstr = " select * from student "
resultList = execSQLcommand(sqlstr).fetchall() #? fetchall() get all data 
print(resultList)                              #? content of the list are full of tuple
for index, content_each_tuple in enumerate(resultList, 0):   #? index從0開始給
    print(index, content_each_tuple)