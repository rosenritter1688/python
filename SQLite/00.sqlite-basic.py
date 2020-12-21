import sqlite3
conn = sqlite3.connect('C:\\Users\\Bruce Ashbee\\Documents\\Python\\SQLite\\std.db')
connecttion = conn.cursor()
t = ('RHAT',)

# connecttion.execute('SELECT * FROM student')
# result = connecttion.fetchall()
#* line 6 ,7 same as below
result = connecttion.execute('SELECT * FROM student').fetchall()

print(result)

for index,content_of_list in enumerate(result,1):
    print(f"{index} : {content_of_list[0]},{content_of_list[1]},{content_of_list[2]}")
# 1 : S001,S001Name,F 
# 2 : S002,S002Name,M 
# 3 : S003,S003Name,F 
# 4 : S004,S004Name,M 
# 5 : S005,S005Name,M 
# 6 : S006,S006Name,M 
# 7 : S007,S007Name,F
# 9 : S009,S009Name,F
# 10 : S010,S010Name,M
for content_of_list in result:
    print(f"{content_of_list[0]},{content_of_list[1]},{content_of_list[2]}")

# S001,S001Name,F
# S002,S002Name,M
# S003,S003Name,F
# S004,S004Name,M
# S005,S005Name,M
# S006,S006Name,M
# S007,S007Name,F
# S008,S008Name,F
# S009,S009Name,F
# S010,S010Name,M