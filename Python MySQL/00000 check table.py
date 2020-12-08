#https://pynative.com/python-mysql-select-query-to-fetch-data/

import mysql.connector
#import mysql.connector  this line imports the MySQL Connector Python module in your program 
#so you can use the methods of this module to communicate with the MySQL database.
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                #We used the mysql.connector.connect()  methods to connect the MySQL Database from Python.
                                         database='electronics',
                                         user='root',
                                         password='Zs8271911c')
    cursor = connection.cursor()
            #we used a connection.cursor methods to get a cursor object from the connection object.
    sql_select_Query = "select * from laptop"
                        # We prepared SQL SELECT query to fetch all rows from a customer table. This table contains four columns.
    cursor.execute(sql_select_Query)#object cursor的執行，去執行select *，
          #executed the select operation using a execute() method of a Cursor object.
    records = cursor.fetchall()#object cursor 的object fetchall method
                     #using a cursor.fetchall()  method we can fetch all the records present under a “Laptop” table.
    print("Total number of rows in the table of customers is: ", cursor.rowcount)

    print("\nPrinting each customer record")
    for row in records:
        print("id = ", row[0], )
        print("Name = ", row[1],)
        print("Price = ", row[2],)
        print("Purchase Date  = ", row[3],"\n")
        ###本来のtable的column順序會有影響唷!!!!!
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

'''


Note:  To fetch data use cursor.execute() to run a query.

    cursor.fetchall() to fetch all rows
    cursor.fetchone() to fetch single row
    cursor.fetchmany(SIZE) to fetch limited rows

'''



