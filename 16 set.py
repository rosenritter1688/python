'''
重點注意事項 set的操作在print裡面都會是不行的比如
print(thiset.add())
都會NO SHOW看不反映
'''


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
        ('{}','unordered','unindexed','*1','No'),##Set
        ('{"":""}','unordered','indexed','YES','')##Dictionary
]
# Create DataFrame object from a list of tuples
hehe = pd.DataFrame(con, columns = ['符號','order','Index編號順序','changeable', 'duplicate members'],
                         index=['List','Tuple','Set','Dictionary'])


print(hehe)
print("*1 = Once a set is created, you cannot change its items, but you can add or remove new items.\n\n")

thisset = {1, 2, 3}##數字的話每次出現順序都依樣!!!!
print(thisset) 
print(type(thisset))
thisset = {"apple", "banana", "cherry"}
print(thisset) ##文字的話每次出現順序不一樣!!!!
'''
Access Items

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, 
or ask if a specified value is present in a set, by using the in keyword.
'''
for x in thisset:
    print(x) ##記得文字出現順序不一樣<但是數字會保持不變>


#? 檢查set裡面的值或內容

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) 
##True
print("juice" not in thisset)
##True




#? Add Items
'''
To add one item to a set use the add() method.

To add more than one item to a set use the update() method.
Example

Add an item to a set, using the add() method:

'''
thisset = {"apple", "banana", "cherry"}
##{'banana', 'apple', 'orange', 'cherry'} 因為set不可以變更再一次宣告一次也沒有用，沒辦法變更裡面的內容
thisset.add("orange")##新增橘子<add.只可以一次增加一個><.update才可以依次多加好幾個>
print(thisset) 
##{'banana', 'apple', 'orange', 'cherry'}
thisset.add("orange")##新增多一次橘子也沒有用，裡面的內容部會有重複
print(thisset) 
##{'banana', 'apple', 'orange', 'cherry'}
thisset.update("A","B","C")
print(thisset)
##{'orange', 'apple', 'C', 'cherry', 'B', 'banana', 'A'}  每次順序不一樣

#? 查裡面有多少個資料

print(len(thisset))
##7


#? remove 去刪除指定內容
#! thisset.remove("D")
#! 會出現錯誤因為set裡面沒有D
#! #Exception has occurred: KeyError
#! 'D'
thisset.remove("A")
print(thisset)
print("------")
##{'banana', 'B', 'apple', 'cherry', 'orange', 'C'} 每次順序都不一樣

#? discard 去刪除指定內容

#! 如果希望刪除指定資料沒有在部會出現ERROR訊息就必須用discard()但是注意方法用不對會出現NONE訊息

##----錯誤方式
print("錯誤方式 ",thisset.discard("A"))
##None
print(thisset.add("A"))
##None
print(thisset.update("1","2","3"))
## !!!no show
print(thisset)
##{'1', '2', 'banana', 'B', 'C', 'cherry', '3', 'A', 'apple', 'orange'}
thisset.discard("2")
print(thisset)
##{'orange', '3', 'banana', 'cherry', '1', 'B', 'C', 'apple', 'A'}

'''
set 沒有index
所以pop()只可以用來刪掉
!!!!random刪掉一個!!!!
不像list和tuple是刪掉最後一個<因為有index>
'''
thisset2 = set(("1","2","3"))
thisset2.pop()
print(thisset2)
thisset2.clear()

'''
用clear清除裡面的資料
'''
print(thisset2)
##set()

'''
比較兩個set
'''
set1 = {"1","2","3"}
set2 = set(("3","4","5"))

print(set1.difference(set2))##拿set1 的內容比較 set2
##{'1', '2'}  ##set1 裡的1 & 2 沒有在set2裡面

'''
	Removes the items in this set that are also included in another, specified set
'''
set1.difference_update(set2)#set1 裡面的3有在set2 裡面所以3會被刪除
print("set1 = ", set1)

'''
找出2個sets裡面有相同的
'''
set3 = {"1","2","3"}
set4 = set(("3","4","5"))
print(set3.intersection(set4))
##{'3'}    #但是不會變更set3 or set4內容
print(set3)
##{'2', '3', '1'}
print(set4)
##{'4', '3', '5'}

'''
比較兩個sets如果沒有的話會被刪除
'''
set3.intersection_update(set4) #set3與set4比較 如果沒有的話會被刪掉  set4不變 
print(set3)
##{'3'}
print(set4)
##{'5', '4', '3'}

'''
union()
不像list不可以用+!!!!!
'''
set5=set(("5","6","7"))
set6=set(("8","9"))
oh = set4.union(set5,set6)##set5 & set6 加到set4 
print(oh)
##{'3', '9', '8', '5', '7', '4', '6'}