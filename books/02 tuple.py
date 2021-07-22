
#! is set to str 
tuple0 = ("only one")
print(isinstance(tuple0,tuple))
##False
print(type(tuple0))
##<class 'str'>

#! method 1 set to tuple
#*最後多一個逗號
tuple02 =("only one",)
print(isinstance(tuple02,tuple))
##True
print(type(tuple02))
##<class 'tuple'>


#! method 2 set to tuple
#*省略誇號
tuple03 = "x","v","k" 
 print(isinstance(tuple03,tuple))
##True
print(type(tuple03))
##<class 'tuple'>