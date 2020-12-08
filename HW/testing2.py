import sqlite3
conn = sqlite3.connect('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\SQLite\\std.db')
c = conn.cursor()
t = ('RHAT',)
c.execute('SELECT * FROM student')
print(c.fetchall())