dic={"A":"APPLE","B":"Boy"}
for key in dic:
    print(dic[key])
# APPLE
# Boy


dict = {"name": "tamago", "color" : "yellow"}

# keyのリストを取得
keyList = dict.keys()
print (keyList)
##dict_keys(['name', 'color'])

# valueのリストの取得
valList = dict.values()
print (valList)
##dict_values(['tamago', 'yellow'])

# keyとvalueのリストの取得
list = dict.items()
print (list)
##dict_items([('name', 'tamago'), ('color', 'yellow')])


for index in valList:
    print(index[1])

