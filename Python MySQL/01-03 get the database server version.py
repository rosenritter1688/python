import mysql.connector
#This line imports the MySQL Connector Python module in your program 
# so you can use this module’s API to connect MySQL.
from mysql.connector import Error
#mysql connector Error object 
# is used to show us an error when we failed to connect Databases 
# or if any other database error occurred while working with the database. 
# Example ACCESS DENIED ERROR when username or password is wrong.

try:
    mydb_connection = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         password='Zs8271911c',
                                         database='Electronics',)
                #mysql.connector.connect()
    # 1 Using this method we can connect the MySQL Database, 
    # this method accepts four required parameters: Host, Database, User and Password 
    #
    # 2 connect() method established a connection to the MySQL database from Python application 
    # and returned a MySQLConnection object.  
    # Then we can use MySQLConnection object to perform various operations on the MySQL Database.
    #
    # 3 The Connect()  method can throw an exception, 
    # i.e. Database error if one of the required parameters is wrong. 
    # For example, if you provide a database name that is not present in MySQL, 
    # then Python application throws an exception. 
    # So check the arguments that you are passing to this method.
    # 
    # connect()
    # Use the connection object returned by a  connect()  method 
    # to create a cursor object to perform Database Operations.
    if mydb_connection.is_connected():
        #is_connected() 
        # is the method of the MySQLConnection class 
        # through which we can verify is our python application connected to MySQL.
        db_Info = mydb_connection.get_server_info()
        '''
        .get_server_info()
        取得server資料
        '''
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb_connection.cursor()
        #.cursor()
        # This method returns a cursor object. Using a cursor object, we can execute SQL queries.
        # The MySQLCursor class instantiates objects that can execute operations such as SQL statements.
        # Cursor objects interact with the MySQL server using a MySQLConnection object.

        cursor.execute("select database();")
        # The cursor.execute() 
        # to execute SQL queries from Python.
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (mydb_connection.is_connected()):
        cursor.close()
        # cursor.close()
        # Using the cursor’s close method we can close the cursor object. 
        # Once we close the cursor object, we can not execute any SQL statement.
        mydb_connection.close()
        # .close()
        # Using the cursor’s close method we can close the cursor object. 
        # Once we close the cursor object, we can not execute any SQL statement.

        print("MySQL connection is closed")
