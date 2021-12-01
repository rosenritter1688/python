


#? FYI 比較運算子
#? < , <=, >, >=, !=, <>, == , in, not in, is, is not
#?                             <> 不等於
#?  結果產生會有bool 就是True & False

#! 邏輯運算子
#!  and , or , not
#! 當and時 只有左右兩邊的物件都為TRUE時，運算結果才會是TRUE，其他結果都為FALSE

li0 = [0,1,2]
li1 = []
li2 = [None,False]

print(li0 and li1)
## [] 
#! empty list is also consider as False


#! 當or時只要左右兩邊其中一個為TRUE 就會得到結果TRUE
print(li1 or li2)


#! not 則是反轉真假值

x = 42

print(0 <= x <= 100)

## TRUE