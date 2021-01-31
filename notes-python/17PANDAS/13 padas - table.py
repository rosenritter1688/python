'''
INSTALL PANDAS FIRST!

win 10 
Step 1 cmd
Step 2 pip install pandas

'''
##import pandas
import pandas as pd   ###後面就不用打pandas 改打pd
import numpy as np
from pandas import DataFrame, Series


# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df, end="\n")### not working
print('table2', end='\n')### not working
#print(df,"\n")
print('table3\n')

# List of tuples
students = [ ('jack', 34, 'Sydeny' , 'Australia') ,
             ('Riti', 30, 'Delhi' , 'India' ) ,
             ('Vikas', 31, 'Mumbai' , 'India' ) ,
             ('Neelu', 32, 'Bangalore' , 'India' ) ,
             ('John', 16, 'New York' , 'US') ,
             ('Mike', 17, 'las vegas' , 'US')  ]
# Create DataFrame object from a list of tuples
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City' , 'Country'], index=['a', 'b', 'c' , 'd' , 'e' , 'f'])

print(dfObj)

# List of tuples
con = [
        ('[]','ordered','indexed','YES','YES'),##List
        ('()','ordered','indexed','YES','YES'),##Tuple
        ('{}','unordered','unindexed','No*1','No'),##Set
        ('{"":""}','unordered','indexed','YES','')##Dictionary
]
# Create DataFrame object from a list of tuples
hehe = pd.DataFrame(con, columns = ['符號','order','Index編號順序','changeable', 'duplicate members'],
                         index=['List','Tuple','Set','Dictionary'])

print(hehe)
print("set is NOT changable BUT updatable")
