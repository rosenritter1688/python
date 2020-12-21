

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
print('--readlinesで一括読み込み--')
#? readlinesで一括読み込み
with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt') as f:
    lines = f.readlines() #! read all and turn it into a list
    print(lines)
    ## ['alpha\n', 'bravo\n', 'charlie\n', 'HELLO\n', 'my\n', 'friend']
    print(type(lines))
    ## <class 'list'>
#! 出來顯示和.read()不一樣! line44~48
#! ITS A list

print("---Loop through the file line by line:---")
#? Loop through the file line by line:
# with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt', newline='') as file_content:
#     for each_line in file_content:
#         print(each_line)
# # alpha

# bravo

# charlie

# HELLO

# my

# friend