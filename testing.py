import random
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as msg
from PIL import ImageTk, Image
 
# Using randrange() to generate numbers from 0-100
print ("Random number from 0-100 is : ",end="")
print (random.randrange(100))
 
# Using randrange() to generate numbers from 50-100
print ("Random number from 50-100 is : ",end="")
print (random.randrange(50,100))
 
# Using randrange() to generate numbers from 50-100
# skipping 5
print ("Random number from 50-100 skip 5 is : ",end="")
print (random.randrange(50,100,12))

list_no = list()
while len(list_no) != 10:
    random_no = random.randrange(0,100,12)
    list_no.append(random_no)
print(list_no)


import random
 
sum = 0
sum1 = 0
count = 0
flag = 0
 
#! while(1):
while True:    
    # generate random number at each turn 1-10
    r1 = random.randrange(1,10)
    r2 = random.randrange(1,10)
     
    # adding to account of players
    sum = sum + r1
    sum1 = sum1 + r2
    count = count+1
     
    print ("Total score of Player 1 after turn %d is :  %d " % (count,sum))
     
    # break when player 1 reaches 100 
    if(sum>=100):
      flag=1
      break
    print ("Total score of Player 2 after turn %d is :  %d" % (count,sum1))
     
    # break when player 2 reaches 100 
    if(sum1>=100):
      flag=2
      break
 
if(flag==1):
   print("\nPlayer 1 wins the game")
else :
   print("\nPlayer 2 wins the game")

