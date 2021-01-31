s = 'aaa' + 'bbb' + 'ccc'
print(s)
# aaabbbccc

s1 = 'aaa'
s2 = 'bbb'
s3 = 'ccc'

s = s1 + s2 + s3
print(s)
# aaabbbccc

s = s1 + s2 + s3 + 'ddd'
print(s)
# aaabbbcccddd


#?+=演算子で連結
#?代入演算子である+=演算子も使える。
#?左辺の文字列変数に右辺の文字列が連結され、代入・更新される。

s1 += s2
print(s1)
<<<<<<< HEAD
# aaabbb


l = ['aaa', 'bbb', 'ccc']
<<<<<<< HEAD
s = '123'.join(l)
print(f"try 1 = {s}")
** try 1 = aaa123bbb123ccc

s = ','.join(l)
print(s)
*@param aaa,bbb,ccc
=======
s = ''.join(l)
print(s)
# aaabbbccc

s = ','.join(l)
print(s)
# aaa,bbb,ccc
>>>>>>> ab3eb57 (first commit)

s = '-'.join(l)
print(s)
# aaa-bbb-ccc

s = '\n'.join(l)
print(s)
# aaa
# bbb
# ccc
=======
# aaabbb
>>>>>>> 8e5dc72be2e34f764c9a33c2c7cf278822bf51ec
