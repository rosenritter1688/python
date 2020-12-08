thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    #index     0         1         2         3        4       5        6
    #index    -7        -6        -5        -4       -3      -2       -1

#? grammer 
#? thislist.insert(index, object)

thislist.insert(1,"aa")
print(thislist)
for index_no, name in enumerate(thislist, 1):
    print(index_no , name)

# 0 apple
# 1 aa #! its insert not replace
# 2 banana
# 3 cherry
# 4 orange
# 5 kiwi
# 6 melon
# 7 mango

#? FYI
#? replace data should be 
thislist[1] = "gum"
print(thislist)
### trying to fix git