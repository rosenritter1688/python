import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="sells_records"
)

mycursor = mydb.cursor()

'''
Using the fetchone() Method

If you are only interested in one row, you can use the fetchone() method.

The fetchone() method will return the first row of the result:
'''



mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()
##只會找第一個資料

print(myresult) 
#as same as below
print(mycursor.fetchmany())

