thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    #index     0         1         2         3        4       5        6
    #index    -7        -6        -5        -4       -3      -2       -1

print(thislist)
print(thislist[1])
## banana
print(thislist[-7])
##apple
print(thislist[-1])#! -1 is last one
## mango
print(thislist[6])
## mango

print(thislist[2:5])#!stop at index 5 and no show
##['cherry', 'orange', 'kiwi']
print(thislist[-5:-2])#!stop at index -2 and no show
##['cherry', 'orange', 'kiwi']

print("從index 2 till last one")
print(thislist[2:])
##['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[:-1])
##['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']