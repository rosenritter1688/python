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
##TABLE is created under database"sells_records"

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
                    CREATE TABLE purchased_list (
                                        user_name varchar(250) NOT NULL, 
                                        user_name_seller varchar(250) NOT NULL,
                                        交易編號 varchar(250) NOT NULL,
                                        purchased_date date NOT NULL,
                                        item_id varchar(250) NOT NULL,
                                        qty INT NOT NULL,
                                        unit_price INT NOT NULL,
                                        total_amount INT NOT NULL,
                                        terms_of_payment varchar(250) NOT NULL,
                                        運送方式 varchar(250) NOT NULL, 
                                        delivery_date DATE NOT NULL,
                                        received_confirm_date DATE NOT NULL,
                                        PRIMARY KEY (user_name, user_name_seller))
                """)

'''
變更TABLE內容
ALTER TABLE `python_db`.`auto_search_for_ingredient` 
ADD COLUMN `location` VARCHAR(45) NOT NULL AFTER `search_po_date`,
ADD COLUMN `search_end_date` DATE NULL AFTER `location`,
CHANGE COLUMN `qty` `qty` INT NOT NULL ,
CHANGE COLUMN `unit_price` `unit_price` INT NOT NULL ,
CHANGE COLUMN `類別` `類別` VARCHAR(45) NOT NULL ,
CHANGE COLUMN `expiry_date` `expiry_date` DATE NOT NULL ,
CHANGE COLUMN `search_po_date` `search_po_date` DATE NOT NULL ;
'''



'''
mycursor.execute("""
                    CREATE TABLE 購物籃 (user_name varchar(250) NOT NULL,
                                        item_id varchar(250) NOT NULL, 
                                        item_name varchar(250) NOT NULL,
                                        qty INT NOT NULL,
                                        unit_price INT NOT NULL,
                                        sub_total INT NOT NULL,
                                        付款有效期限 date NOT NULL, 
                                        PRIMARY KEY (user_name, item_id))
                """)
'''













