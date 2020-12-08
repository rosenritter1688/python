import mysql.connector
from mysql.connector import Error

def getLaptopDetail(id):
    try:
        mySQLConnection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Zs8271911c",
        database="sells_records"
        )

        cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = """select * from customers where id = %s"""
        cursor.execute(sql_select_query, (id,))
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

id1 = 1
id2 = 2
getLaptopDetail(id1)
getLaptopDetail(id2)
getLaptopDetail(3)
