'''
Primary Key

When creating a table, you should also create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

We use the statement "INT AUTO_INCREMENT PRIMARY KEY" 
which will insert a unique number for each record. Starting at 1, and increased by one for each record.
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="Electronics"
)

mycursor = mydb.cursor()
##create table and assign ky at the same time
'''
mycursor.execute("CREATE TABLE cu (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") 
'''
##assign ky if table is already created
'''
mycursor.execute("ALTER TABLE laptop ADD PRIMARY KEY (Id); COMMIT")
'''