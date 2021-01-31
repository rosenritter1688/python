import os
#? check if file exists

if os.path.exists("C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\sample.txt"):
    print("the file exist")
else:
    print("the file is not exist")
#the file exist

#? check if folder exists
if os.path.exists("C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\hi"):
    print("the folder exist")
else:
    print("the folder is not exist")
    with open("C:\\Users\Bruce Ashbee\\Documents\\Python 2020\筆記\\FILE HANDLING\\hi\\","w"): 
        print("folder created")

#the folder exist