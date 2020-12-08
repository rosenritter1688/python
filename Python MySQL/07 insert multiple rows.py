import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="sells_records"
)

mycursor = mydb.cursor()


'''
Insert Multiple Rows

To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, 
containing the data you want to insert:




Example

Fill the "customers" table with data:
'''

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]



mycursor.executemany(sql, val)

mydb.commit()
##Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.


print(mycursor.rowcount, "was inserted.") 


'''
打在MySQL Workbench 
'''

'''
INSERT INTO laptop (Id, Name, Price, Purchase_date) VALUES
(1, 'Lenovo ThinkPad P71', 6459, '2019-08-14'),
(2, 'Area 51M', 6999, '2019-04-14'),
(3, 'MacBook Pro', 2499, '2019-06-20'),
(4, 'HP Pavilion Power', 1999, '2019-01-11'),
(5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
(6, 'Microsoft Surface', 2330, '2019-07-23'),
(7, 'Acer Predator Triton', 2435, '2019-08-15')
'''