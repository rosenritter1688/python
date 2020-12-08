

#create functions that returns a Boolean Value:
def myFunction() :
  return True       ##RETURN 只可以用在FUNCTION
print("5", myFunction())
##5 Ture

def myFunction2() :
  return False  #影響6 or 7 會出來


if myFunction2() == False: #被省略掉也依樣
  print("6. YES!")
else:
  print("7. NO!")
##6 YES!

if myFunction2() == True: #同下  ##! 因為前面myFunction2只會return False 所以只會跑到else
  print("8. YES!")
else:
  print("9. NO!")
##print("9. NO!")



