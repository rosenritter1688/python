


#! "w" - Create a new file if it does not exist:
#! "x" - Create - will create a file, returns an error if the file exist
#! "a" - Append - will create a file if the specified file does not exist


           
myF = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\筆記\\FILE HANDLING\\write.txt", "w") 
#! 不指定路徑的話會創在以下路徑 C:\Users\Bruce Ashbee\Documents  >>>VS CODE the folder that you open
if myF != None:       #!如果創立檔案成功
    myF.write("3 X 3 乘法表\n------------------\n")
for i in range(1,4):
    for j in range(1,4):
        myF.write("{0:2d}x{1:2d} = {2:2d}\n".format(i, j,i * j)) #write(只能有一個參數)
myF.close()




print("==== string object with whole file / readline() =======")
myF = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\筆記\\FILE HANDLING\\write.txt","r") # r:readonly
if myF != None:
    print(myF.read())
myF.close()



print("==== list/ readlines() =======")
myF = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\筆記\\FILE HANDLING\\write.txt","r") # r:readonly
if myF != None:
   lines = myF.readlines() # read into a list[]
   for oneline in lines:
       print(oneline)
myF.close()

with open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\筆記\\FILE HANDLING\\sample.txt","r") as f:
    content = f.read()
    print(content)