

#TODO https://note.nkmk.me/python-function-def-return/     reseach needed
'''
Arbitrary Arguments, *args

If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
'''

def my_function(*kids):
    #!如果你不曉得會有幾個argument,在argument前面打*
    #! This way the function will receive a tuple of arguments, and can access the items accordingly:
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
##The youngest child is Linus



def my_function2(*kids):   #! 因為加了*所以kids引數會是tuple
    print("The youngest child is " + str(kids))
                                    ##kids)  不可以因為未出現ERROR 
                                    ##can only concatenate str (not "tuple") to str
my_function2(("Emil", "Tobias", "Linus"))
##The youngest child is (('Emil', 'Tobias', 'Linus'),)
                      #!(                            )   代表著是tuple
                                                #!  , tuple 裡面只有一個值的話最後面會有一個, 除非值超過1個才不會有  line 37 ~ 42 got examples

my_function2(["Emil", "Tobias", "Linus"])       #! [] 用了還是一樣是tuple
##The youngest child is (['Emil', 'Tobias', 'Linus'],)

my_function2("Emil", "Tobias", "Linus")
##The youngest child is ('Emil', 'Tobias', 'Linus')
#!                      (                         )   代表是tuple



tuple_kids = ("Emil", "Tobias", "Linus")
print(type(tuple_kids))
##<class 'tuple'>
tuple_kids = ("Emil")
print(type(tuple_kids))
##<class 'str'>