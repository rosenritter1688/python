import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c"
)
print(mydb) 


mycursor = mydb.cursor() 
           #カーソルをオープンします
##https://software.fujitsu.com/jp/manual/manualfiles/M070075/J2X01638/01Z200/sqlbg04/sqlbg033.html

'''
カーソルの概念

カーソルは、表の中の1行を特定する仮想的な道具です。
カーソルを使用して処理の対象とする行を特定しておいて、
その行からデータを取り出したり、その行を更新したり、
または削除したりすることができます。カーソルにより行を特定することを、カーソルを位置づけるといいます。

カーソルには、オープンされている状態と、クローズされている状態の2つがあります。一度もオープンされていないカーソルは、クローズされている状態と同じです。カーソルを使用してデータの操作ができるのは、オープンされている状態のときです。

オープンされた状態のカーソルは、表の特定の行を位置づけているときと、そうでないときがあります。カーソルの概念を理解しやすくするために、カーソルの位置には以下の4通りがあると考えます。
'''
'''
Create Database
'''
mycursor.execute("CREATE DATABASE Electronics") ##create a database named sells_records

##if the database exists will comes out a ERROR MESSAGE

##Exception has occurred: DatabaseError
##1007 (HY000): Can't create database 'sells_records'; database exists

'''
Check if Database Exists
Method 1
'''

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

'''
Check if Database Exists
Method 2
you can try to access the database when making the connection:
'''