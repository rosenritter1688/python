
#! "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#! "a" - Append - Opens a file for appending, creates the file if it does not exist       從尾端寫入
#! "w" - Write - Opens a file for writing, creates the file if it does not exist
#! "x" - Create - Creates the specified file, returns an error if the file exists
#! "t" - Text - Default value. Text mode
#! "b" - Binary - Binary mode (e.g. images)
'''
In addition you can specify if the file should be handled as binary (e.g image) or text mode
f = open("demofile.txt", "rt")
'''


'''
初心者向けにPythonのread, readline, readlinesメソッドの使い方について解説しています。
ファイルサイズが小さい場合は、readメソッドで一括に読み込んでも問題ありませんが、
ファイルサイズが大きい場合はサイズ指定をしたり、
readlineメソッドで少しずつ読み込むことも出来ます。
'''

'''
read, readline, readlinesメソッドとは
read, readline, readlinesメソッドは、いずれもファイルの内容を読み出す時に用います。
'''


print('--sample.txt---')
print("alpha")
print("bravo")
print("charlie")
print('--end of sample.txt---\n\n')
    


#? readでサイズ指定あり
#?readはファイルから指定サイズのデータを読み出します。
#!引数を省略すると、ファイルの内容全てを読み出します。

print("readでサイズ指定あり")
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
    contents = f.read(10)#!read 10 characters, space included
    print(contents)
##alpha
##brav
#*1つ目はread(サイズ指定あり)のケースです。10を指定したので、「alphaObrav」を読み込みました(Oは改行コード)
                                                          #!空格也算一個，包括空格一共有十個


print('--readでサイズ指定なしすべてを読み込む-')
#? readでサイズ指定なし
#?　すべてを読み込む
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
    contents = f.read()
    print(contents)
#alpha
#bravo
#charlie

print('--readlineで1行だけ読み込み--')

#? readlineで1行だけ読み込み
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
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

print('--readlinesで一括読み込み--')
#? readlinesで一括読み込み
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
    lines = f.readlines() #! read all and turn it into a list
    print(lines)
    print(type(lines))
#[‘alpha\n’, ‘bravo\n’, ‘charlie\n’]
#<class 'list'>
#! 出來顯示和.read()不一樣! line44~48
#! ITS A list

print("---Loop through the file line by line:---")
#? Loop through the file line by line:
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\sample.txt') as f:
    for a in f:
        print(a)
#alpha

#bravo

#charlie

