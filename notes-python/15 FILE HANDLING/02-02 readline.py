

#! "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#! "a" - Append - Opens a file for appending, creates the file if it does not exist       從尾端寫入
#! "w" - Write - Opens a file for writing, creates the file if it does not exist
#! "x" - Create - Creates the specified file, returns an error if the file exists
#! "t" - Text - Default value. Text mode
#! "b" - Binary - Binary mode (e.g. images)
#? readでサイズ指定あり
#?readはファイルから指定サイズのデータを読み出します。
#!引数を省略すると、ファイルの内容全てを読み出します。
"""Sample.txt
alpha
bravo
charlie
HELLO
my
friend
"""


print('--readlineで1行だけ読み込み--')

#? readlineで1行だけ読み込み
with open(r"C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt") as f:
    line = f.readline()
    print(line)
#alpha

print('--read first 2 lines--')
#? readline to read first 2 lines
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
    print(f.readline())
    print(f.readline())
#alpha
#bravo