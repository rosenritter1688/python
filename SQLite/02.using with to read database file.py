import sqlite3


#!win 10
#connect_To_Database = sqlite3.connect("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\SQLite\\std.db")
#!mac
#connect_To_Database = sqlite3.connect("//Users//bruceashbee//Documents//SQLite//std.db")

''' #?"with" grammer example from file handling 
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
    lines = f.readlines() #! read all and turn it into a list
'''

''' #?"with" grammer example from internet for SQL
with conn.cursor() as curs:
    curs.execute(SQL)
'''
'''#!working
MAC
'''
with sqlite3.connect("//Users//bruceashbee//Documents//SQLite//std.db") as datafile_readed:
    result = datafile_readed.execute(" select * from student ").fetchall()#? fetchall() get all data
    print(result,"\n",type(result)) #? content of the list are full of tuple
    ##<class 'list'>
    for index, content_each_tuple in enumerate(result, 0):   #? indexing result從0開始給
        print(index, content_each_tuple)
'''#!windows

with sqlite3.connect("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\SQLite\\std.db") as datafile_readed:
    result = datafile_readed.execute(" select * from student ").fetchall()#? fetchall() get all data
    print(result,"\n",type(result)) #? content of the list are full of tuple
    for index, content_each_tuple in enumerate(result, 0):   #? indexing result從0開始給
        print(index, content_each_tuple)

'''