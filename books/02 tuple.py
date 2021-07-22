
#! is set to str 
tuple0 = ("only one")
print(isinstance(tuple0,tuple))
##False
print(type(tuple0))
##<class 'str'>




#! method 1 set to tuple
#*省略誇號
tuple03 = "x","v","k" 
print(isinstance(tuple03,tuple))
##True
print(type(tuple03))
##<class 'tuple'>

print(tuple03)
##('x', 'v', 'k')

#! tuple03[0] = "asa"
##'tuple' object does not support item assignment
#! coz tuple is 不可變
#! 除非重新指定tuple03
tuple03 = "ask","v","k" 
print(tuple03)

##('ask', 'v', 'k')``
#! tuple物件是不可變所以不需要擔心別名現象，

#! method 2 set to tuple with 1 element only
#*最後多一個逗號
tuple02 =("only one",)
print(isinstance(tuple02,tuple))
##True
print(type(tuple02))
##<class 'tuple'>