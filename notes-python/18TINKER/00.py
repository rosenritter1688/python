import requests
import sqlite3
def execSQLcommand(sqlstr):
    global myConn
    global myCursor
    try:
      myCursor = myConn.execute(sqlstr)
      myConn.commit()
      print("指令已成功執行:" + sqlstr)
      return myCursor
    except:
      print("指令有誤:", sqlstr)
def qo(instr):
    return "'" + instr + "'"
myConn = sqlite3.connect("C:\\Users\\Bruce Ashbee\\Documents\\Python\\SQLite\\std.db")
myCursor = myConn.cursor()

 

websource = requests.get('https://datacenter.taichung.gov.tw/swagger/OpenData/e0c55c8f-1c74-47ce-909c-8ecacbfaaeb7')
#print("websource:", type(websource)) #<class 'requests.models.Response'>
myJson = websource.json()
#print(type(myJson)) #myJson is a list
sqlstr = 'delete from test'
execSQLcommand(sqlstr)
for idx , content in enumerate(myJson,0): 
    print("====================")
    print("idx={0}, content={1}".format(idx, content))
    #print("content type:", type(content)) #content is a dictionary
    print("---")
    
    sqlstr = " insert into test(conuty_name, county_id, family_Num, religion, profession, Voluntary, rd, val_year) values("
    for key in content:
        #print("key:", key, "value:", content[key] )
        sqlstr += qo(content[key]) + "," 
    sqlstr = sqlstr[0:-1] + ")"
    execSQLcommand(sqlstr)

 

    print(sqlstr)