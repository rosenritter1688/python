'''
Use a Python variable in an Update query to update MySQL table
'''

import mysql.connector
from mysql.connector import Error

def updateLaptopPrice(id,price):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='electronics',
                                             user='root',
                                             password='Zs8271911c')

        cursor = connection.cursor()
        sql_update_query = """Update laptop set price = %s where id = %s"""  
        inputData = (price, id)
        cursor.execute(sql_update_query, inputData)
        connection.commit()
        print("Record Updated successfully ")
        

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


updateLaptopPrice(1, 80)
updateLaptopPrice(2, 100)