'''
Let’s see you want to execute Following SELECT SQL Query and 
store the table’s column value into a python variable for further processing.

cursor.execute("SELECT Price FROM Laptop WHERE id = 21")
print (cursor.fetchone() )

You can get the output like

{u'Price': u'7000'}

However, how to select just the column value 7000 and save it in a variable to do some calculations?

You need a laptop price into a variable so you can give a 10% discount on it. 
To do this calculation, you can select column value and store it in a python variable. 
Let see how to do this with an example.

Python Program to Select MySQL table’s column value into Variable
'''


import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='electronics',
                                         user='root',
                                         password='Zs8271911c')

    sql_Query = "select price from laptop where id =%s"
    id = (1,)#id 號碼設定一號
    cursor = connection.cursor()
    cursor.execute(sql_Query, id) #找設定ID一號的資料
    record = cursor.fetchone()

    # selecting column value into varible
    price = float(record[0]) * 10 ##如果想要打折改這邊
    print("Laptop price is : ", price)

except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")