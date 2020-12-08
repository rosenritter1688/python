import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='electronics',
                                         user='root',
                                         password='Zs8271911c')
    cursor = connection.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from Laptop where id = 1"""  #讀取id 1號的資料
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)#show data b4 update

    # Update single record now
    sql_update_query = """Update Laptop set Price = 900 where id = 1"""  #更新id 1號的資料為7000
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
