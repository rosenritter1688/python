
#! https://techacademy.jp/magazine/28688
#? join関数とは
#?join関数とは、文字列や数字などを新しい文字列として連結させる関数です。
#?例を示すと「こんにちは」と「さようなら」を「,」で連結させて「こんにちは,さようなら」という文字列を取得したいときに使用します。
l = ['aaa', 'bbb', 'ccc']
s = '123'.join(l)
print(f"s = {s}")
##try 1 = aaa123bbb123ccc

s = ','.join(l)
print(s)
## aaa,bbb,ccc

s = '-'.join(l)
print(s)
# aaa-bbb-ccc

s = '\n'.join(l)
print(s)
# aaa
# bbb
# ccc


#! List 裡面有數字就不可以只用join(),必須要先用map()把數值也轉成文字才可以用
'''error code sample

list = ['My', 'name', 'is', '山田', '太朗。', 15, "歳です"]
str = ' '.join(list)
print(str)
'''
list = ['My', 'name', 'is', '山田', '太朗。', 15, "歳です"]
number_inside_list_all_converted_to_string = map(str, list)
join_list = ' '.join(number_inside_list_all_converted_to_string)
print(join_list)
## My name is 山田 太朗。 15 歳です


