import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="Electronics"
  
)
'''
Creating a Table

To create a table in MySQL, use the "CREATE TABLE" statement.

Make sure you define the name of the database when you create the connection
'''
mycursor = mydb.cursor()
#簡單版的
'''
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''
##ERROR msg will be given if the table exists
##TABLE is created under database"sells_records"

#If this page is executed with no error, you have successfully created a table named "customers".


##複雜版的

mycursor.execute("""
                    CREATE TABLE use2r (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        user_name varchar(250) NOT NULL,passsword varchar(250) NOT NULL,
                        email varchar(250) NOT NULL,
                        create_date date NOT NULL)
                """)