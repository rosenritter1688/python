<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
'''
/*
 ! Red
 ? Blue
 * Green
 ^ Yellow
 & Pink
 ~ Purple
 todo Mustard
 // Grey
*/
'''
'''
#TODO 文字列、タプルをソートする方法

#!文字列、タプルはイミュータブル（更新不可）なので、元のオブジェクトを書き換えるsort()メソッドは用意されていない。
=======
文字列、タプルをソートする方法

文字列、タプルはイミュータブル（更新不可）なので、元のオブジェクトを書き換えるsort()メソッドは用意されていない。
<<<<<<< HEAD
>>>>>>> ab3eb57 (first commit)

一方、ソートしたリストを新たなオブジェクトとして生成するsorted()関数の引数にはリストだけでなく文字列やタプルも指定できる。ただし、sorted()が返すのはリストなので、文字列やタプルに変換する処理が必要となる。
=======
一方、ソートしたリストを新たなオブジェクトとして生成するsorted()関数の引数にはリストだけでなく文字列やタプルも
指定できる。ただし、sorted()が返すのはリストなので、文字列やタプルに変換する処理が必要となる。
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
文字列のソート

sorted()関数の引数に文字列を指定すると、ソートされた文字列の一文字ずつが要素として格納されたリストが返される。
<<<<<<< HEAD
'''
<<<<<<< HEAD
=======

>>>>>>> ab3eb57 (first commit)
org_str = 'cebad'

new_str_list = sorted(org_str)
print(org_str)
print(new_str_list)
# cebad
# ['a', 'b', 'c', 'd', 'e']

=======

org_str = 'cebad'

new_str_list = sorted(org_str)
print(f'org_str = \"{org_str}\"')
print(f'new_str_list = \"{new_str_list}\"')
# cebad
# ['a', 'b', 'c', 'd', 'e']
'''
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
source: sort_sorted.py

文字列のリストを連結して一つの文字列にするにはjoin()メソッドを使う。

<<<<<<< HEAD
    関連記事: Pythonで文字列を連結・結合（+演算子、joinなど）

new_str = ''.join(new_str_list)
print(new_str)
# abcde

source: sort_sorted.py

まとめて書いてもOK。降順にソートしたい場合は引数reverseをTrueとする。

=======
関連記事: Pythonで文字列を連結・結合（+演算子、joinなど）
'''
new_str = ''.join(new_str_list)
print(new_str)
# abcde
'''
source: sort_sorted.py

まとめて書いてもOK。降順にソートしたい場合は引数reverseをTrueとする。
'''
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
new_str = ''.join(sorted(org_str))
print(new_str)
# abcde

new_str_reverse = ''.join(sorted(org_str, reverse=True))
print(new_str_reverse)
# edcba
<<<<<<< HEAD

=======
'''
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
source: sort_sorted.py

文字列の大小関係は文字のUnicodeコードポイント（文字コード）によって決まる。以下の記事を参照。

    関連記事: Pythonで文字列を比較（完全一致、部分一致、大小関係など）

<<<<<<< HEAD
タプルのソート

タプルについても文字列と同様。sorted()関数の引数にタプルを指定すると、要素がソートされたリストが返される。

=======

タプルのソート

タプルについても文字列と同様。sorted()関数の引数にタプルを指定すると、要素がソートされたリストが返される。
'''
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
org_tuple = (3, 1, 4, 5, 2)

new_tuple_list = sorted(org_tuple)
print(org_tuple)
print(new_tuple_list)
# (3, 1, 4, 5, 2)
# [1, 2, 3, 4, 5]
<<<<<<< HEAD

=======
'''
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
source: sort_sorted.py

リストからタプルへの変換はtuple()を使う。

    関連記事: Pythonでリストとタプルを相互に変換するlist(), tuple()
<<<<<<< HEAD

new_tuple = tuple(new_tuple_list)
print(new_tuple)
# (1, 2, 3, 4, 5)

source: sort_sorted.py

まとめて書いてもOK。降順にソートしたい場合は引数reverseをTrueとする。

=======
'''
new_tuple = tuple(new_tuple_list)
print(new_tuple)
# (1, 2, 3, 4, 5)
'''
source: sort_sorted.py

まとめて書いてもOK。降順にソートしたい場合は引数reverseをTrueとする。
'''
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
new_tuple = tuple(sorted(new_tuple_list))
print(new_tuple)
# (1, 2, 3, 4, 5)

new_tuple_reverse = tuple(sorted(new_tuple_list, reverse=True))
print(new_tuple_reverse)
# (5, 4, 3, 2, 1)
