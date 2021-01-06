

# import requests





# with open(r'C:\Users\Bruce Ashbee\Documents\Python\notes-python\FILE HANDLING\sample.txt','r') as f:
#     lines = f.readlines()[1:]
#     print(lines)
# ## ['bravo\n', 'charlie\n', 'HELLO\n', 'my\n', 'friend']
# for changed_data in lines:
#     print(changed_data.replace('\n', ""))
    




import csv
import requests

CSV_URL = 'https://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv'


with requests.Session() as s:
    download = s.get(CSV_URL)
decoded_content = download.content.decode('utf-8')
    ## print(type(decoded_content))
    ## <class 'str'>
    #print(decoded_content)
    ##醫事機構代碼,醫事機構名稱,醫事機構地址,醫事機構電話,成人口罩剩餘數,兒童口罩剩餘數,來源資料時間
    ##0145080011,衛生福利部花蓮醫院豐濱原住民分院,花蓮縣豐濱鄉豐濱村光豐路４１號,8358141,1922,360,2020/12/21 17:26:24
    ##0291010010,連江縣立醫院,連江縣南竿鄉復興村２１７號,623995,0,310,2020/12/21 17:26:24
cr = csv.reader(decoded_content.splitlines(), delimiter=',')
my_list = list(cr)
## <class 'list'>
print(type(my_list))
# for row in my_list:
#     if "南投" in row[2]:
#         print(row)
    ## ['5938080048', '中寮健保藥局', '南投縣中寮鄉永安街１３６號', '(049)2691940', '1017', '580', '2020/12/21 17:29:25']
