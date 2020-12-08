def findwhileEven():
  loopGo = "Y"
  while loopGo == "Y":
    x = int(input("pls input a number"))
    if x%2 == 0:     #if x divided by 2 餘數是零，表是可以整除
       print(str(x) + " is a even")         # can use var + "string"
    else:            #do not forget abt :
       print(str(x) , " is a oddd")         # can use var , "string" is the same
    loopGo = input("Pls enter Y for continue")   #! coz line 2 loopGo = Y so will to endless loop
findwhileEven()