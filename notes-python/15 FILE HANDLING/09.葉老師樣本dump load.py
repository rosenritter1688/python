
import  pickle as pk
#write
myFileOutput = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\筆記\\FILE HANDLING\\binaryData.dat","wb") #第2個參數加b, 其他同文字檔
pk.dump("Password:",myFileOutput)  #dump:將資料寫入2進位檔
pk.dump(123456789,myFileOutput)
myFileOutput.close()
#read
myFileInput = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\筆記\\FILE HANDLING\\binaryData.dat","rb")
print(pk.load(myFileInput), pk.load(myFileInput))#load()從檔案讀出時, 順序與格式同 dump的順序

myFileInput.close()
