

#?リスト型のメソッド sort(): 元のリストをソート
#?sort()はリスト型のメソッド。

    #**4. 組み込み型 — Python 3.6.1 ドキュメント
    #**https://docs.python.org/ja/3/library/stdtypes.html#list.sort
#!元のリスト自体が書き換えられる破壊的処理。

org_list = [3, 1, 4, 5, 2]
org_list.sort()
print(org_list)
# [1, 2, 3, 4, 5]



#!sort()が返すのはNoneなので注意。
print(org_list.sort())
# None



#?デフォルトは昇順。降順にソートしたい場合は引数reverseをTrueとする。
org_list.sort(reverse=True)
print(org_list)
# [5, 4, 3, 2, 1]

