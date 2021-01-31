

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
print("readでサイズ指定あり")
with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt',"rt") as f:
    contents = f.read(10)#!read 10 characters, space included
    print(contents)
##alpha
##brav
#*1つ目はread(サイズ指定あり)のケースです。10を指定したので、「alphaObrav」を読み込みました(Oは改行コード)
                                                            #!跳行也算一個
                                                            #!空格也算一個，包括空格一共有十個
print('--readでサイズ指定なしすべてを読み込む-')
with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt',"rt") as f:
    contents = f.read()  #? readでサイズ指定なし,すべてを読み込む
    print(contents)
#alpha
#bravo
#charlie