
#fucion also have pass like if statement
##if b > a:
##  pass

#def ads():
#    pass
def print_msg(s):
    print(s)
s = "hello"
print(s)
##Hello
s = str(input("pls enter a msg u wanna pass to : "))
print(print_msg(s))
##will print out any u entered

print("------------------------------------------------------")

x = 5
def sum_up():#sum of started from 1 added it all up to 10
    global x #funcion 外面的變數Ｘ拿進來用~>通常FUNCTION的變數就算和外面變數一樣但是不一樣的，需要共用的話需要加global
    x = 4

sum_up()
print("checking up x value = ",x," which is no longer 5")
##4  x is not 5 becuase of the function sum_up change the value

'''
--------------------------ARGUMENT引數-----------------------------------------
* 翻譯為引數的原文為 Argument
當你呼叫函式的時候, 你可以放在括號內的東西

參數的原文為 Parameter
放在函式的標記式, 用來說明這個函式, 當它被呼叫時必須接收到什麼樣的資料,

Information can be passed into functions as arguments.

Arguments are specified after the function name, 
inside the parentheses. You can add as many arguments as you want, 
just separate them with a comma.

The following example has a function with one argument (fname). 
When the function is called, 
we pass along a first name, which is used inside the function to print the full name: 

#? def 函數名稱 (引數argument)
'''


def my_function_fname(fname):  #fnmae = arguments
    print(fname + " Refsnes")

my_function_fname("Emil")  #parameter   "Emil" #放在函式的標記式, 用來說明這個函式, 當它被呼叫時必須接收到什麼樣的資料,
my_function_fname("Tobias")
my_function_fname("Linus")
'''
Emil Refsnes
Tobias Refsnes
Linus Refsnes
'''
print("**********************")
'''
Number of Arguments
引數的數量
By default, a function must be called with the correct number of arguments. 
Meaning that if your function expects 2 arguments, 
you have to call the function with 2 arguments, not more, and not less. 
'''

def my_function_name(fname, lname):
    print(fname + " " + lname)

my_function_name("Emil", "Refsnes")
##Emil Refsnes
#! my_function("Emil")
#! you have to call the function with 2 arguments, not more, and not less. 
'''ERROR msg
        my_function() missing 1 required positional argument: 'lname'
'''





def my_function3(child3, child2, child1):
  print("The youngest child is " + child3)

my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus") ##這個方式順序沒關係

'''
Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
Example

If the number of keyword arguments is unknown, add a double ** before the parameter name:
'''

def my_function4(**kid):
  print("His last name is " + kid["lname"])

my_function4(fname = "Tobias", lname = "Refsnes") 
##His last name is Refsnes 

def my_function5(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function5(fruits)

'''
Return Values

To let a function return a value, use the return statement:
Example
'''

def my_function(x):
  return 5 * x

print(my_function(3))##15
print(my_function(5))##25
print(my_function(9))##454