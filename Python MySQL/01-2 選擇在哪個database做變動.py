import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Zs8271911c",
  database="sells_records"  
  ##the database that u wanna access when making connection
  ##後面的動作都是變動都會在在名為sells_records的database
  
) 
##If executed with no error, the database "sells_records" exists in your system


