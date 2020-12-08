'''
short hand if
'''
a = 3
b = 2
if a > b: print("a > b")
'''
Short Hand If ... Else
'''
print("a > b") if a > b else print("b > a")

''' 
You can also have multiple else statements on the same line:
'''
### three condition
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
                         # statement 2
                         # print("=") if a == b
# statement 1 
# print("A") if a > b
                                              # statement 3
                                              # else print("B") 
##=
###CONDITION 1
###print("A") if a > b
###CONDITION 2 
###else print("=") if a == b
###CONDITION 3 
###else print("B")
'''
print("A") 
if a > b:
    else:
        print("=") if a == b:
    else: 
        print("B")
'''


'''
pass

if statement 後面不可以是空的！！！
The pass Statement
if statements cannot be empty, 
but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.
'''
a = 33
b = 200

if b > a:
  pass


