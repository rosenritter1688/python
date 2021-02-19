
#! リストを連結/結合して文字列化【joinメソッド】
#* joinメソッドを使うと、文字列のリストやタプルを一つの文字列に連結することができます。次のように書きます。
#* grammer
#* "区切り文字".join(リストまたはタプル)



#リストを作ります。
list = ["Tom", "Jerry", "Betty"]
 
#join()メソッドでリスト内の文字列を連結します。
string = ", ".join(list)
 
#確認しましょう。
print(string)
## Tom, Jerry, Betty

#リストを作ります。
list = ["Tom", "Jerry", "Betty"]
 
#それぞれjoin()メソッドで違う区切り文字を入れて連結します。
string_a = " ".join(list) #空白区切り
string_b = " and ".join(list) # and 区切り
 
#確認しましょう。
print(string_a)
print(string_b) 
## Tom Jerry Betty
## Tom and Jerry and Betty

#? 数値を含むリストを文字列化したい場合は、次のようにmap関数と組み合わせて使います。


''' map関数を使えば、数値を含むリストでもjoinメソッドで文字列化できます。 '''
list = ['a', 1, 'b', 2]
map_list = map(str, list)
print(' and '.join(map_list))
## a and 1 and b and 2





