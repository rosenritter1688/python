

#!color
#*color
#?color
#todo
#! "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#! "a" - Append - Opens a file for appending, creates the file if it does not exist       從尾端寫入<<cant read file>>
#! "w" - Write - Opens a file for writing, creates the file if it does not exist
#! "x" - Create - Creates the specified file, returns an error if the file exists

'''
In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode (default)
"b" - Binary - Binary mode            (e.g. images)


f = open("demofile.txt", "rt")
'''
#----------------------------------------------------------------------------------------------------------------------
#?Write to an Existing File
#?To write to an existing file, you must add a parameter to the open() function:
#?"a" - Append - will append to the end of the file
#?"w" - Write - will overwrite any existing content

#!CREATE a file
with open("C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\sample2.txt","w") as file_content:  #! "a" 寫入尾端
    file_content.write("HELLO")


#!DELETE a file
import os
os.remove("C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\sample2.txt") 