sqlcommand = "select std_id , std_name from student "
staddate = execSQLcommand(sqlstr).fetchall()
selectedItem = StringVar(value=itemList[0])
stdList