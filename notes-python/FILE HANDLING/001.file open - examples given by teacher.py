



'''
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.
'''
#*The key function for working with files in Python is the open() function.
#*The open() function takes two parameters; filename, and mode.
#*There are four different methods (modes) for opening a file:
#* open("FILE NAME<with file directry>", "MODE")

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





           
myF = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\write.txt", "w") 
#! 不指定路徑的話會創在以下路徑 C:\Users\Bruce Ashbee\Documents  >>>VS CODE the folder that you open
if myF != None:       #!如果創立檔案成功
    myF.write("44 乘法表\n------------------\n")
for i in range(1,5):
    for j in range(1,5):
        myF.write(f"{i:02d} x {j:02d} = {i * j:02d}\n") #write(只能有一個參數)
myF.close()
print("file clsed")





print("====read() starts=======")
myF = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\write.txt","r") # r:readonly
if myF != None:
   print(myF.read())
myF.close()

print("=====read() ends======")




'''
myF = open("write.txt","r") # r:readonly
if myF != None:
   lines = myF.readlines() # read into a list[]
   for oneline in lines:
       print(oneline)
myF.close()
'''






