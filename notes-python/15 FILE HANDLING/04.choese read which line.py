import linecache
#!linecache は 1 から始まるのに注意してください
#?指定讀取第幾行


#!color
#*color
#?color
#todo
#! "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#! "a" - Append - Opens a file for appending, creates the file if it does not exist       從尾端寫入
#! "w" - Write - Opens a file for writing, creates the file if it does not exist
#! "x" - Create - Creates the specified file, returns an error if the file exists

'''
In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)


f = open("demofile.txt", "rt")
'''



print('--sample.txt---')
print("alpha")
print("bravo")
print("charlie")
print('--end of sample.txt---\n\n')

line = linecache.getline('C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\sample.txt',2)
print(line)
#bravo


with open('C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\sample.txt'):
    line = linecache.getline('C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\sample.txt',2)
    print(line)
#bravo

