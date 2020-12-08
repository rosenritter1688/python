'''
The break Statement
With the break statement we can stop the loop even if the while condition is true:
中斷迴圈
'''


print("#1############################")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
##1
##2
##3
print("#2############################")
i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break
##1
##2
'''

'''
print("#3############################")
i = 1
while i < 6:
    i += 1
    print(i)
    if i == 3:
        break
##2
##3




