import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="python_db"
  )
'''
Creating a Table

To create a table in MySQL, use the "CREATE TABLE" statement.

Make sure you define the name of the database when you create the connection
'''
mycursor = mydb.cursor()

'''
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''
##ERROR msg will be given if the table exists
##TABLE is created under database"python_db"<line 7>

#If this page is executed with no error, you have successfully created a table named "customers".


'''
mycursor.execute("""
                    CREATE TABLE 上架 (
                        item_id INT NOT NULL PRIMARY KEY,
                        user_name varchar(250) NOT NULL,
                        qty INT NOT NULL,
                        unit_price INT NOT NULL,
                        類別 varchar(45) NOT NULL,
                        expiry_date date NOT NULL,
                        po_date date NOT NULL)
                """)
'''



mycursor.execute("""
                    CREATE TABLE auto_search_for_ingredient (
                        ingredient_name varchar(45),
                        user_name varchar(250) NOT NULL,
                        qty INT,
                        unit_price INT,
                        類別 varchar(45),
                        expiry_date date,
                        search_po_date date,
                        PRIMARY KEY (ingredient_name, user_name)) 
                        
                """)
                        ##PRIMARY KEY (ingredient_name, user_name)) 
                        ##2 pk = Composite Primary Key


