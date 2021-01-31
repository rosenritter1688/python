#https://note.nkmk.me/python-enumerate-start/
#Python, enumerateの使い方: リストの要素とインデックスを取得
                                        #index    



##TUPLE也可以用enumberate



seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
print(seasons)
##['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
##[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
####注意line 25 拿掉enumberate又會變成沒有index了
list(enumerate(seasons, start=1))                               #index 從1號開始編
'''
沒有指定開始號碼都會從0開始編index
'''
print(list(enumerate(seasons, start=1)))
###[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]



##次と等価です:
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

'''
通常のforループ
'''


l = ['Alice', 'Bob', 'Charlie']

for name in l:
    print(name)
# Alice
# Bob
# Charlie
'''
source: enumerate_start.py
enumerate関数を使ったforループ

enumerate()関数の引数にリストなどのイテラブルオブジェクトを指定する。

インデックス番号, 要素の順に取得できる。
'''


for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie


'''
enumerate関数のインデックスを1から開始

上の例のように、デフォルトだとenumerate()関数のインデックスは0から始まる。

0以外の数値から開始したい場合は、enumerate()関数の第二引数に任意の開始数値を指定する。

1からはじめる場合。

'''

for i, name in enumerate(l, 1):
    print(i, name)
# 1 Alice
# 2 Bob
# 3 Charlie

#下のと同じく効果がある

for i, name in enumerate(l, start=1):
    print(i, name)


'''
もちろん他の数字からでもOK。
'''
for i, name in enumerate(l, 42):
    print(i, name)
# 42 Alice
# 43 Bob
# 44 Charlie

'''
連番の文字列を作りたい場合に便利。1から始めるためにi+1にしたりするよりはenumerate()関数の第二引数で開始数値を指定したほうがスマート。
'''

for i, name in enumerate(l, 1):
    print('{:03}_{}'.format(i, name))
# 001_Alice
# 002_Bob
# 003_Charlie
