import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Zs8271911c",
        database="sells_records"
        )

    mycursor = mydb.cursor()

    '''
    Using the fetchone() Method

    If you are only interested in one row, you can use the fetchone() method.

    The fetchone() method will return the first row of the result:
    '''



    mycursor.execute("SELECT * FROM customers")

    print(mycursor.fetchmany(10))    ##找前十個資料
    
except Error as e:   ##跟最前面有個try:(LINE 4,LINE 2)跟這個是一隊一組的
    print("Error reading data from MySQL table", e)
finally:
    if (mydb.is_connected()):
        mydb.close()
        cursor.close()
        print("MySQL connection is closed")