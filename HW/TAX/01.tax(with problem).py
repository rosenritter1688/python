'''
公式：應納稅額 = 綜合所得淨額 X 稅率 – 累進差額

綜合所得淨額 	                 稅率 	 累進差額
TWD0         – TWD540,000 	     5%  	TWD0
TWD540,001   – TWD1,210,000   	12% 	TWD37,800
TWD1,210,001 – TWD2,420,000 	20% 	TWD134,600
TWD2,420,001 – TWD4,530,000 	30% 	TWD376,600
TWD4,530,001 以上 	            40%     TWD829,600
'''

'''
讀入檔案/課堂教材/income.txt, 算出應繳所得稅, 寫出結果至tax.txt, 格式如下, 所得稅計算可參考https://www.money101.com.tw/blog/%e8%bc%95%e9%ac%86%e8%a7%a3%e6%9e%902020%e5%b9%b4%e6%89%80%e5%be%97%e7%a8%85%e7%b4%9a%e8%b7%9d%e8%88%87%e8%a9%a6%e7%ae%97%e6%96%b9%e5%bc%8f
ID:身分證字號 如 A000000001
城市: 如 A
收入: 如 1000000
所得稅:   $$,$$$
------------------ 
ID:身分證字號 如 B000000001
城市: 如 B
收入: 如 1500000
所得稅:   $$,$$$
-----------------
'''

'''

#! 可能抓步道最後面一個數字!!!! 改用split做了
'''


original_list = list()
changed_list = list()

#A000000001, A, 500000
#012345678901234567890

print("---Loop through the file line by line:---")
#? Loop through the file line by line:
with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\HW\\TAX\\income.txt',"r+") as f:
    for a in f:
        id = a[:10]
        #id = A000000001
        area = a[12]
        #area = A
        income = a[15:-1] #! 可能抓步道最後面一個數字!!!! 改用split做了
        #income = 500000
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
        print("城市: = " + area)
        print(f"收入: {int(income)}")
        print(f"所得稅: ${int(tax):,}")
        print("----------------------------------------------\n")
        #original_list.append([id,area,income,int(tax)])
        #print(original_list)
        #print(type(original_list),"\n")
        with open('C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\HW\\TAX\\tax.txt',"a") as tax_data:   #! "a" - Append - Opens a file for appending, creates the file if it does not exist 
            tax_data.write(f"{id}, {area}, {income}, {int(tax)}\n")


#! 可能抓步道最後面一個數字!!!! 改用split做了

#for x in original_list:
#    print(x)