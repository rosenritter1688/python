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


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    #index     0         1         2         3        4       5        6
    #index    -7        -6        -5        -4       -3      -2       -1
print("all list")
print(thislist)
print("show last one")
print(thislist[-1])
print(thislist[6])
print("show first 1")
print(thislist[0])
print(thislist[-7])
print("Return the third, fourth, and fifth item:")
print(thislist[2:4],"this is wrong because index 4 is excluded")
##['cherry', 'orange'] this is wrong because index 4 is excluded
print(thislist[2:5])
##['cherry', 'orange', 'kiwi']
print(thislist[-5:-2])#index -2 will be not included
##['cherry', 'orange', 'kiwi']
print("SHOW前四個!!!!!!最不一樣的別搞混")
print(thislist[:4]) #SHOW前面四個不是到show到index 4
##['apple', 'banana', 'cherry', 'orange']


'''
print list 用法
print(*list1) 
##11 5 17 23
print(str, list1)
##<class 'str'> [11, 5, 17, 23]

'''



'''
Change Item Value
To change the value of a specific item, refer to the index number:
'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
    print(x)

'''
Check if Item Exists

To determine if a specified item is present in a list use the in keyword:
'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

if thislist[2] == "banana":
  print("Yes thislist[1] it's banana")
else:
    print("No, thislist[1] its not banana")

'''
List Length

To determine how many items a list has, use the len() function:
'''
print(len(thislist))

'''
Add Items

To add an item to the end of the list, use the append() method:
加到list的最後面
'''
thislist.append("kiwi")
print(thislist)
'''
To add an item at the specified index, use the insert() method:
指定資料加到index號碼
'''
thislist.insert(1,"mango")
print(thislist)

'''
刪除list裡面其中一個資料
'''

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
#thislist.remove("apple","cherry") ### 每一次只可以刪掉一個資料



'''
The pop() method removes the specified index, (or the last item if index is not specified):

'''
thislist = ["apple", "banana", "cherry"]
thislist.pop() #不指定index就會刪除最後一個
print(thislist)
##['apple', 'banana']
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)#指定index刪除資料
print(thislist)
##['apple', 'cherry']
thislist = ["apple", "banana", "cherry"]
thislist.pop(-1)#指定index刪除資料
print(thislist)
##['apple', 'banana']
'''
The del keyword removes the specified index:
'''
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
##['banana', 'cherry']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del thislist[2:3]
print("**************")
print(thislist)
##['apple', 'banana', 'orange', 'kiwi', 'melon', 'mango']

'''
用del刪除整個list
list裡面的資料以及list的容器名稱都沒了!!!!
要保留list的容器要用clear()
'''
thislist = ["apple", "banana", "cherry"]
del thislist
#~~~~~~~~~~~~~~~~~~print(thislist)~~~~~~~~~~~~~~~~~~~~~~~
####this will cause an error because you have succsesfully deleted "thislist".
###NameError: name 'thislist' is not defined
'''
The clear() method empties the list:
用clear()清空list裡面的資料
或是用
thislist = []
'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#~~~~~~~~~~~相同於 thislist = []

thislist = None         ###把容器變成未知
print(thislist)
##None
thislist = []
print(thislist)
##[]

'''
COPY list內容到另一個地方
.copy()

You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.
不可以只是單純打list2 = list1, 
因為list2 只是會變成是list1的參考名稱
在lis1做任何改變都會自動做相同的改變到list2

'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
##['apple', 'banana', 'cherry']
###錯誤示範用list2 = THISLIST
thislist = ["apple", "banana", "cherry"]
list2 = thislist
thislist.pop(1)
print(thislist)
##['apple', 'cherry']
print(list2)
##['apple', 'cherry']
'''
built-in method list() for copying list
'''

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
##['apple', 'banana', 'cherry']

'''
Join 2 lists together
+
'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
##['a', 'b', 'c', 1, 2, 3]

'''
用for loop & append 來將兩個list相加
'''
list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]
for x in list5:
  list4.append(x)
print(list4)
['a', 'b', 'c', 1, 2, 3]

'''
USE expand()
to join 2 list together
'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
##['a', 'b', 'c', 1, 2, 3]

'''
use list(())
創造新的list創造新的list
'''
thislist = list(("apple", "banana", "cherry"))
print(thislist)

['apple', 'banana', 'cherry']

'''
刪除list裡面多筆資料
數字篇
use for loop
Method 1
'''
# Python program to remove multiple 
# elements from a list 

# creating a list 
list1 = [11, 5, 17, 18, 23, 50] 

# Iterate each element in list 
# and add them in variale total 
for ele in list1: 
	if ele % 2 == 0: 
		list1.remove(ele) 

# printing modified list 
print("New list after removing all even numbers: ", list1) 
##New list after removing all even numbers:  [11, 5, 17, 23]

'''
Method 2
'''
list1 = [11, 5, 17, 18, 23, 50] 

# will create a new list, 
# excluding all even numbers 
list1 = [ elem for elem in list1 if elem % 2 != 0] 

print(*list1) 
##11 5 17 23
print(*list1)
'''
cx = (*list1)
print(cs.replace(" ",""))
用不了這個方式!!!!!!!!!!!!
'''
print(str, list1)
##<class 'str'> [11, 5, 17, 23]

'''
Example #4: Using list comprehension

Let’s say the elements to be deleted is known, instead of the indexes of those elements.
In this case, we can directly eliminate those elements without caring about indexes which we will see in next example.
'''
# creating a list 
list1 = [11, 5, 17, 18, 23, 50]  
# items to be removed 
unwanted_num = {11, 5}   
list1 = [ele for ele in list1 if ele not in unwanted_num] 
print(list1)
##[17, 18, 23, 50]  
# printing modified list 
print("New list after removing unwanted numbers: ", list1) 
##New list after removing unwanted numbers:  [17, 18, 23, 50]



thislist = ["apple", "banana", "cherry"]
if "juice" in thislist:
  print("Yes, 'apple' is in the fruits list") 
else:
  thislist.append("juice")
print(thislist)
print("---------------------")


thislist = ["apple", "banana", "cherry"]
if "juice" not in thislist:
  thislist.append("juice")  
else:
  print("'juice' is added in the fruits list") 

print(thislist)

print("--------要保留的資料----下面都有有問題---------")

list1 = [11, 5, 17, 18, 23, 50]  

unwanted_num = [11, 5]  # items to be kept
for ele in list1:
  if ele not in unwanted_num:
    list1.remove(ele)
print(list1)
##[11, 5, 18, 50]
list1 = [11, 5, 17, 18, 23, 50]  
unwanted_num = [11, 5]  # items to be kept
for ele in list1:
  if ele in unwanted_num:
    continue
  else:
    list1.remove(ele)
print(list1)
##[11, 5, 18, 50]

print(11 not in list1)

##False

if 11 not in list1 == False:
  list1.remove(11)
print(list1)
##[11, 5, 18, 50]