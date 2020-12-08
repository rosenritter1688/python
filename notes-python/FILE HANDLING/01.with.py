

#?Pythonのwith構文とは
#!Pythonのwithを使用すると、何かの処理の開始時と終了時に必須の処理を、絶対に実行してくれます。
#!何かの処理の開始時と終了時に必須の処理とは、通信処理やファイル処理やデータベース処理などがあります。


#?Pythonでwithを使う文法
#!with 開始と終了を必要とする処理


"""
"r":唯讀
"w":覆蓋原內容
"a":從尾端寫入
"r+": r + w   ( +:表示增加更新功能)
"w+": 覆蓋原內容 r+w
"a+": r+w
"""

'''
#! NOT using with
'''


#?withを使用しない場合
#?ファイル処理コード

fileread = open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\income.txt", "r")#open関数を利用してtechacademy.txtを読み込む(r)為に開いています(open)。
#開いた内容をfileread変数に代入しています
print(fileread.read())#fileread変数に対して、read関数を使用して読み込みながら、print関数を使用して表示をしています。
fileread.close()#開いたファイルを閉じています。この処理を忘れるとエラーになります。


print("--------------")









#?withを使用する場合
#?ファイル処理コード
with open("C:\\Users\\Bruce Ashbee\\Documents\\Python 2020\\notes-python\\FILE HANDLING\\income.txt", "r") as fileread:
    print(fileread.read())
#一定要空格 OR TAB!!!

#1行目のwith open(“techacademy.txt”, “r”) as fileread:では、open関数を利用してtechacademy.txtを読み込む(r)為に開いています(open)。
#その際、開いたファイル名をas fileread変数名に代入しています。
#!先頭にwithを記載しているのでclose( )関数の処理はありません。
#2行目のprint(fileread.read( ))では、fileread変数に対して、read関数を使用して読み込みながら、print関数を使用して表示をしています。
#!繰り返しますが、先頭にwithを記載しているのでclose( )関数の処理は必要ありません。これにより、開いたファイルを閉じる処理を忘れずに自動的に行うことが可能です。
#!結果的にエラーを防ぐ事が可能です。


