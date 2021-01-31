
"""content of sample.txt
alpha
bravo
charlie
HELLO
my
friend
"""

#! Method 1

with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt', 'r') as f:
    lines = next(f)
    print(lines) #this will print out the first line
    ## alpha
    for line in f:
        print(line.replace("\n",""))
# bravo

# charlie
       
# HELLO  
       
# my     
       
# friend 

#!  Method 2 and will trun it into list data 

with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt','r') as f:
    lines = f.readlines()[1:]
    print(lines)
## ['bravo\n', 'charlie\n', 'HELLO\n', 'my\n', 'friend']
for changed_data in lines:
    print(changed_data.replace('\n', ""))
    
