'''
Python Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments,
 but can only have one expression.
'''
'''
Syntax
lambda arguments : expression 

'''
###example 1
x = lambda a: a + 10
         　   #a = argument引數 可以很多個
    　　　  　 #a + 10 是運算公式只可以有一個
print(x(5))
##15

###example 2
x = lambda a,b : a + b
print(x(10,2)) #set a as 1 and b as 2
##12





'''
Why Use Lambda Functions?

The power of lambda is better shown 
when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number:
'''

def myfunc(n):
  return lambda a : a * n
               #a = argument引數 可以很多個
               #a * n 是expression只可以有一個
'''
Use that function definition to make a function that always doubles 
the number you send in:
'''
mydoubler = myfunc(2)#set n as 2
mytripler = myfunc(3)#set n as 3

'''
wrong usage
'''
print(myfunc(3))
##<function myfunc.<locals>.<lambda> at 0x0000029183FA9AF0>
'''
correct usage
'''
print(mydoubler(11)) #set a as 11 
##22
print(mytripler(1)) #set a as 1
##3