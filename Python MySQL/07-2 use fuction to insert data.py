##https://pynative.com/python-mysql-insert-data-into-database-table/

import mysql.connector
from mysql.connector import Error

def insertVariblesIntoTable(name, address):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='sells_records',
                                             user='root',
                                             password='Zs8271911c')
        
        mySql_insert_query = """INSERT INTO customers (Name, address) 
                                VALUES (%s, %s) """

        recordTuple = (name, address)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into customer table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable('Area 51M','2019-04-14')
insertVariblesIntoTable('MacBook Pro','2019-06-20')


##TABLE裡面的ID是KY而已早就已經設定會自動編號所以不用輸入ID


##輸入ID的方式
##如果要輸入到ID3但此ID已經被占用會出現錯誤訊息
##Failed to insert into MySQL table 1062 (23000): Duplicate entry '3' for key 'customers.PRIMARY'
