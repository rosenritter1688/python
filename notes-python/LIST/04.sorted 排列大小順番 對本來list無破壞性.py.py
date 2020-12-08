

#?組み込み関数 sorted(): ソートした新たなリストを生成


#?sorted()は組み込み関数。

    #*2. 組み込み関数 sorted() — Python 3.6.1 ドキュメント
    #*https://docs.python.org/ja/3/library/functions.html#sorted

#?引数にソートしたいリストを指定するとソートされたリストを返す。
#!元のリストは変更されない非破壊的処理。

org_list = [3, 1, 4, 5, 2]

new_list = sorted(org_list)
print(org_list)
print(new_list)
# [3, 1, 4, 5, 2]
# [1, 2, 3, 4, 5]


#? sort()と同様にデフォルトは昇順。降順にソートしたい場合は引数reverseをTrueとする

new_list_reverse = sorted(org_list, reverse=True)
print(org_list)
print(new_list_reverse)
# [3, 1, 4, 5, 2]
# [5, 4, 3, 2, 1]
