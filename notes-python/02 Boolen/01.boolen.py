
#?Most Values are True
#?Almost any value is evaluated to True if it has some sort of content.

print(bool(True))
##* True
print(bool(False))
## False 
print(bool(None))
## False
print(bool(0))   #! Any number is True, except 0.  
## False
print(bool(15))
#* True
print(bool(""))  #! Any string is True, except empty strings.
## False
print(bool(" ")) 
#* True
print(bool(()))  #! Any list, tuple, set, and dictionary are True, except empty ones.
## False
print(bool([]))
## False
print(bool({})) 
## False
