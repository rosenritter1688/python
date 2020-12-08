import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="sells_records"
)

mycursor = mydb.cursor()
'''
Insert Into Table

To fill a table in MySQL, use the "INSERT INTO" statement.
Example

Insert a record in the "customers" table:
'''
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

print(mycursor.rowcount, "record inserted.")
               #rowcount 檢查剛剛有輸入幾個ROW也就是有幾個資料的意思


##資料會重複但是PK並部會依樣COZ會有不同的ID<--前面設定的PK適用ID


'''
FOR WORKBENCH

INSERT INTO customers (name, address) VALUES ("Bruce", "amber st")
'''

