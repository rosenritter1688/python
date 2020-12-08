data_list=list()

with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\HW\\TAX\\income.txt',"r+") as f:
    for a in f:
        x = a.split(", ")
        print(x)
        data_list.append(x)
        print(data_list)
for id,city,income in data_list:
    print(id,city,income)
    if float(income) >= 4530001:
        tax = (float(income) * 0.4) - 829600
    elif (float(income) >= 2420001) & (float(income) <= 4530000):
        tax = (float(income) * 0.3) - 376600
    elif (float(income) >= 1210001) & (float(income) <= 2420000):
        tax = (float(income) * 0.2) - 134600
    elif (float(income) >= 540001) & (float(income) <= 1210000):
        tax = (float(income) * 0.12) - 37800
    else:
        tax = (float(income) * 0.05)
    print("ID:身分證字號: " + id)
    print("城市: = " + city)
    print(f"收入: ${int(income):,}")
    print(f"所得稅: ${int(tax):,}")
    print("----------------------------------------------\n")
    with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\HW\\TAX\\tax.txt',"a") as tax_data:   #! "a" - Append - Opens a file for appending, creates the file if it does not exist 
        s_income = str(income)
        s_tax =str(tax)
        tax_data.write("{}, {}, {}, {}\n".format(id.strip(),city.strip(),s_income.strip(),s_tax.strip())) #! strip() 刪除左右兩邊的空白!!!有時候會有

