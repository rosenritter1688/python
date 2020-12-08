import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="sells_records"
)

mycursor = mydb.cursor()

'''
Select From a Table

To select from a table in MySQL, use the "SELECT" statement:
Example

Select all records from the "customers" table, and display the result:
'''

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
##Note: We use the fetchall() method, 
# which fetches all rows from the last executed statement.
for x in myresult:
  print(x)