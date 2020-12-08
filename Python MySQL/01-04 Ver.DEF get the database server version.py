import mysql.connector
#This line imports the MySQL Connector Python module in your program 
# so you can use this module’s API to connect MySQL.
def get_connection():
    connection = mysql.connector.connect(host="127.0.0.1",
                                         user="root",
                                         password="Zs8271911c",
                                         database="python_db")
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection() #呼叫DEF line 3
        cursor = connection.cursor() 
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to MySQL version: ", db_version)
        close_connection(connection) #呼叫def 
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 1: Print Database version")
read_database_version()

