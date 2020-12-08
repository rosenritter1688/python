'''
INSTALL PANDAS FIRST!

win 10 
Step 1 cmd
Step 2 pip install pandas

'''
##import pandas
import pandas as pd   ###後面就不用打pandas 改打pd

# List of tuples
con = [
        ('[]','ordered','indexed','YES','YES'),##List
        ('()','ordered','indexed','NO','YES'),##Tuple
        ('{}','unordered','unindexed','No*1','No'),##Set
        ('{"":""}','unordered','indexed','YES','')##Dictionary
]
# Create DataFrame object from a list of tuples
hehe = pd.DataFrame(con, columns = ['符號','order','Index編號順序','changeable', 'duplicate members'],
                         index=['List','Tuple','Set','Dictionary'])


print(hehe)
print("*1 = Once a set is created, you cannot change its items, but you can add or remove new items.\n\n")


thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #不包括index 5同list

'''
Change Tuple Values
照理說Tuple不能變更資料但是可以利用轉換成list在做變更
再轉回成Tuple
'''
x = ("apple", "banana", "cherry")
y = list(x)  #convert it to list
y[1] = "kiwi"
x = tuple(y) #convert it back to Tuple
print(*x) 
##apple kiwi cherry

print(len(x))
##3

'''
One item tuple, remember the commma:
不加的話會是str
'''

thistuple = ("apple",)
print(type(thistuple))
##<class 'tuple'>
thistuple = ("apple") #NOT a tuple
print(type(thistuple))

##<class 'str'>

'''
不像list可以用del刪除個別的資料
但是跟list依樣可以把整個tuple刪掉
'''
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists 

'''
join two tuples
+
'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

'''
跟list 依樣可以用(())創造新的tuple

'''

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

'''
Python has two built-in methods that you can use on tuples.
Method 	    Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
'''

print(thistuple.index("apple"))
##0
print(thistuple.count("banana"))
##1

tuple2 = tuple(("hehe","hehe","hehe","hehe","hehe","hehe","hehe","hello"))
print(tuple2.count("hehe"))
##7
print(tuple2.count("hello"))
##1
print(tuple2.index("hehe"))
##0