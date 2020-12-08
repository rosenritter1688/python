import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="sells_records"
)

mycursor = mydb.cursor()

'''
Get Inserted ID

You can get the id of the row you just inserted by asking the cursor object.

Note: If you insert more than one row, the id of the last inserted row is returned.
'''

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)


mydb.commit()
##Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.


print("1 record inserted, ID:", mycursor.lastrowid) 
