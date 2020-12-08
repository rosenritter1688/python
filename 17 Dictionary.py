'''
INSTALL PANDAS FIRST!

win 10 
Step 1 cmd
Step 2 pip install pandas

'''
##import pandas
import pandas as pd
###後面就不用打pandas 改打pd

# List of tuples
con = [
        ('[]','ordered','indexed','YES','YES'),##List
        ('()','ordered','indexed','NO','YES'),##Tuple
        ('{}','unordered','unindexed','*1','No'),##Set
        ('{"":""}','unordered','indexed','YES','')##Dictionary
]
# Create DataFrame object from a list of tuples
hehe = pd.DataFrame(con, columns = ['符號','order','Index編號順序','changeable', 'duplicate members'],
                         index=['List','Tuple','Set','Dictionary'])


print(hehe)
print("*1 = Once a set is created, you cannot change its items, but you can add or remove new items.\n\n")

#!                 符號      order  Index編號順序 changeable   duplicate members
#!List             []    ordered    indexed        YES               YES
#!Tuple            ()    ordered    indexed         NO               YES
#!Set              {}  unordered  unindexed         *1                No
#!Dictionary  {"":""}  unordered    indexed        YES
#!   *1 = Once a set is created, you cannot change its items, but you can add or remove new items.

'''
create a new dictionary
2 way2
'''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

'''
找資料方式有兩種
'''

print(thisdict["model"])
##Mustang
print(thisdict.get("model"))
##Mustang


'''
Change value
'''
thisdict["year"] = 1982
print(thisdict["year"])
##1982

'''
Print all key names in the dictionary, one by one:
'''
for x in thisdict:
        print(x)
##brand
##model
##year
print("\n\n\n")
'''
an other way of showing keys
'''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("an other way of show key items")
print(thisdict.keys())
##dict_keys(['brand', 'model', 'year'])


'''
Print all values in the dictionary, one by one:
Method I for loop & print(thisdist[x])
'''
for x in thisdict:
        print(thisdict[x])
##Ford
##Mustang
##1982
print("--------")
'''
Print all values in the dictionary, one by one:
Method II  .value()
'''
for x in thisdict.values():
        print(x)
##Ford
##Mustang
##1982


print("----item() & loop for key names and values----")
'''
items() method
loop through both keys and values
'''
for x,y in thisdict.items():
        print(x,y)
##brand Ford
##model Mustang
##year 1982
print("--------")

'''
Check if Key item Exists
'''
if "model" in thisdict:
        print("yes model is in the dictionary")
else:
        print("it is not exist in the dictionary")

print("-----")

'''
check for values
'''

if "Ford" in thisdict.values():  ##"1964"此方式沒辦法檢查1964是否存在value!!--->改成1964就可以
                                                                              #因為its int          
        print("yes value 1964 is in the dictionary")
else:
        print("no this couldnt be found in the key items of the dictionary")
'''
len()
檢查有幾組資料
'''


print(len(thisdict))
##3

'''
add items
跟 變更value一樣
注意打錯key name 就會變成新增
'''
##print(thisdict["color"] = "red")
##cant not do in this way
print("add items METHOD I")
thisdict["color"] = "red"
print(thisdict)
##{'brand': 'Ford', 'model': 'Mustang', 'year': 1982, 'color': 'red'}
print("--------")
print("add items METHOD II")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

'''
Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
'''
print("增加新的key name and value")

thisdict = {            ##重新命名一次資料會被改!!!  前面的COLOR : RED 不見了
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["colors"] = "RED,BLUE","YELLOW","k"    ##可以放兩個以上的values進去到同一個key items 裡面
print(thisdict)
##{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'colors': ('RED,BLUE', 'YELLOW', 'k')}


if "k" in thisdict:  ##this is only checking key items 
        print("yes it is in the dictionary")
else:
        print("no this couldnt be found in the key items of the dictionary")
#no this couldnt be found in the key items of the dictionary


if "Ford" in thisdict.values():  ##"1964"此方式沒辦法檢查1964是否存在value!!--->改成1964就可以
        print("yes value 1964 is in the dictionary")
else:
        print("no this couldnt be found in the key items of the dictionary")

for x,y in thisdict.items():  ##可以順利找出多個values('RED,BLUE', 'YELLOW', 'k')
        print(x,y)
##brand Ford
##model Mustang
##year 1964
##colors ('RED,BLUE', 'YELLOW', 'k')

'''
delete the whole dictionary


del thisdict 
print(thisdict) #this will cause an error because "thisdict" no longer exists.
.clear()方法才會保留dist但是清空裡面的內容
'''

'''
REMOVING key items and its value
METHOD I
.pop()

'''
thisdict = {
        "brand":"ford",
        "model":"Mustang",
        "year":"1964",
}
thisdict.pop("year")
print(thisdict)
##{'brand': 'ford', 'model': 'Mustang'}
'''
REMOVING key items and its value
METHOD II
del thisdist["model"]
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
##{'brand': 'Ford', 'year': 1964}

'''
刪除最後插入的key items and value
.popitem()
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
##{'brand': 'Ford', 'model': 'Mustang'}

'''
.clear()
'''

thisdict.clear()
print(thisdict)
##{}

'''
2 ways of copy disctionary

copy()

dict()
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dist1 = thisdict.copy()
print(dist1)
##{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

dist2 = dict(dist1)
print(dist1)
##{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


'''
Nested Dictionaries
A dictionary can also contain many dictionaries, this is called nested dictionaries
'''

myfamily = {
        "child1":{
                "name":"h",
                "age":"18",
        },
        "child2":{
                "name":"b",
                "age":"19"
        },
        "wife":{
                "name":"C",
                "age":"35"
        },
}
print(myfamily)
'''
結合三個現有的DICT成為一個NEST DICT
'''

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


'''
fromkeys()

USE TUPLE () or list [] to
create a dict with 3 keys all with value 0
'''

x = ['key1', 'key2', 'key3']
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
##{'key1': 0, 'key2': 0, 'key3': 0}

'''
Definition and Usage
The fromkeys() method returns a dictionary with the specified keys and the specified value.

Syntax
dict.fromkeys(keys, value)
Parameter Values
Parameter	Description
keys	Required. An iterable specifying the keys of the new dictionary
value	Optional. The value for all keys. Default value is None
'''

x = ('key1', 'key2', 'key3')
#沒設定values 就會是預設值None
thisdict = dict.fromkeys(x)  

print(thisdict)


'''
setdefault()


'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")  ##ATTENTION!!!! 如果設定default時key items 不存在就會存進dictionary裡面

print(x)##White
print(car)                      
##{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco") ##ATTENTION!!!! 如果設定default時key items 存在!並不會變更dictionary裡面內容

print(x)##Mustang
print(car)
##{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
