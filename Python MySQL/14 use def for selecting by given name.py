import mysql.connector
from mysql.connector import Error

def getLaptopDetail(search):
    try:
        mySQLConnection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Zs8271911c",
        database="sells_records"
        )
                                        # we set buffered=True in connection. Cursor () method to avoid MySQL Unread result error.
        cursor = mySQLConnection.cursor(buffered=True)
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
        
        sql_select_query = """SELECT * from customers where name = %s""" # %s == argument "search" (line 4 & 31)
        cursor.execute(sql_select_query, (search,)) 
                                        #def getLaptopDetail的引數search  (line4)
        record = cursor.fetchall()

        for row in record:
            print("Name = ", row[0], )
            print("Address = ", row[1])
            print("ID = ", row[2], "\n")


    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if (mySQLConnection.is_connected()):
            cursor.close()
            mySQLConnection.close()
            print("MySQL connection is closed")

getLaptopDetail("John")

##就算Table 有兩個John也抓得出來
'''
Name =  John
Address =  Highway 21     
ID =  1

Name =  John
Address =  Highway 21     
ID =  2
'''