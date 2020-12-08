import mysql.connector
#import mysql.connector  this line imports the MySQL Connector Python module in your program 
#so you can use the methods of this module to communicate with the MySQL database.
mydb = mysql.connector.connect(
      #We used the mysql.connector.connect()  methods to connect the MySQL Database from Python.
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="sells_records"
)

mycursor = mydb.cursor()

'''

Selecting Columns

To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):






Example

Select only the name and address columns:

'''

print("------use fetchall-------")
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x) 

for row in myresult:
  print("Name = ", row[0], )
  print("Address = ", row[1])
  print("ID = ", row[2], "\n")







print("---------use fetchmany---------------")
mycursor.execute("SELECT name FROM customers") ##這個要再輸入一次不然部會得到資料
myresult2 = mycursor.fetchmany()#不設定數字DEFAULT是1
print(myresult2)
##[('John',), ('John',), ('Bruce',)]
#for x in myresult2:
#  print(x)
##('John',)
##('John',)
##('Bruce',)

