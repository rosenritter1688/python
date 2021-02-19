

#! USE map method to turn variables in list or tuple into int
#! even if some variables in the list(or tuple) itselfs are integer already


''' map関数を使えば、数値を含むリストでもjoinメソッドで文字列化できます。 '''
list = ['a', 1, 'b', 2]
#! turn all values in the list into str
map_list = map(str, list)
print(' and '.join(map_list))
## a and 1 and b and 2

map_list = map(str, list)
print(", ".join(map_list))


#! cant turn all into int
list2 = ["3", "1", "4", "2"]
aakl = map(int,list2)
print(aakl)

list3 = []
for a in aakl:
    print(a,type(a))
    ##3 <class 'int'>
    ##1 <class 'int'>
    ##4 <class 'int'>
    ##2 <class 'int'>
    list3.append(a)
print(list3)
## [3, 1, 4, 2]

new_list =[]
test_list = ['1', 4, '3', '6', '7'] 
#! 注意list裡面有一個int only
for a in test_list:
    new_list.append(int(a))
print(new_list)

#! another method from geekForgeek
test_list2 = ['1', 4, '3', '6', '7']
#! 注意list裡面有一個int only
for i in range(0, len(test_list2)): 
    test_list2[i] = int(test_list2[i]) 
print ("Modified test_list2 is : " + str(test_list2))