'''
Python MySQL update Multiple Rows data in a single query

It is possible to update multiple rows in a single SQL Query. 
you can also call it a bulk update. 
We can use a cursor.executemany() method of cursor object to update multiple tables rows.
'''
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='electronics',
                                         user='root',
                                         password='Zs8271911c')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Price = %s where id = %s"""
    # multiple records to be updated in tuple format
    records_to_update = [(3000, 3), (2750, 4)]
    cursor.executemany(sql_update_query, records_to_update)
    connection.commit()

    print(cursor.rowcount, "Records of a laptop table updated successfully")

except mysql.connector.Error as error:
    print("Failed to update records to database: {}".format(error))
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
