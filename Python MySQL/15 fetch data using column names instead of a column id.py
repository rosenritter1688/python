'''
Python Fetch MySQL data using the column names instead of a column id

In some scenarios, We need to retrieve the SQL result column value using column name 
instead of the column index in Python. For example, you would like to something like this.

records = cursor.fetchall()

for row in records:
    val1 = row["columnName1"], )
    val2 = row["columnName2"])
	val3 = row["columnName3"])

If you try to fetch data using column name directly, you will receive a 
TypeError: tuple indices must be integers or slices, not str.

To selected records from my MySQL table using a column name, 
we only need to change the cursor creation. Replace the standard cursor creation 
with the following code, and you are ready to fetch records 
from my MySQL table using a column name.

cursor = connection.cursor(dictionary=True)

Why set dictionary=True?  because MySQLCursorDict creates a cursor that returns rows as dictionaries 
so we can access using column name (here column name is the key of the dictionary)

Now, Let’s see the example. In the following case, 
I have selected all the records from my MySQL table using a column name 
instead of the integer index of the column.

'''
##跟第十個有甚麼差別不大懂
##cursor = connection.cursor(dictionary=True) 
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='Electronics',
                                         user='root',
                                         password='Zs8271911c',
                                         )

    
    cursor = connection.cursor(dictionary=True) 
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    sql_select_Query = "select * from Laptop"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Fetching each row using column name")

    for row in records:
        id = row["Id"]
        name = row["Name"]
        price = row["Price"]
        purchase_date = row["Purchase_date"]
        print(id, name, price, purchase_date)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

