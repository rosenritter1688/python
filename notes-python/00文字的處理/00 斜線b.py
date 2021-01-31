print("Who are you?\b ") 
print("Who are you?\b") #後面有打字\b才會有效


#print("{}階層值是{}".format(m,r))

def fabs(n):
    if n != 2:
        return n * fabs(n-1)
    else:
        return 2
print(5, fabs(5))