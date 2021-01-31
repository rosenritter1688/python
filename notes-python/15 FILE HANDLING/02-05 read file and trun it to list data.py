#!  Method 2 and will trun it into list data 

with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt','r') as f:
    lines = f.readlines()[1:]
    print(lines)
## ['bravo\n', 'charlie\n', 'HELLO\n', 'my\n', 'friend']
for changed_data in lines:
    print(changed_data.replace('\n', ""))
    