
#TODO search needed  https://www.headboost.jp/python-try-except/

#! NameError,ZeroDivisionError,TypeError,ValueError
#! 不可以改名字這些是專有個錯誤代數エラーオブジェクト

try:
    print(a)
except NameError as e:  #  ←変数にエラーオブジェクトを代入。
    print(e)  #  ←  変数をexceptブロックで出力して内容を確認できる。
    print('変数aの値が定義されていません。')
except ZeroDivisionError as e: 
    print(e)  
    print('0での割り算は行えません。')
except TypeError as e:  
    print(e)  
    print('文字列と数値は連結できません。')
except ValueError as e: 
    print(e)  
    print('型変換が不正です。')
##変数aの値が定義されていません。

try:
    num = 2/0
except NameError as e:  
    print(e)  
    print('変数aの値が定義されていません。')
except ZeroDivisionError as e:  
    print(e)  
    print('0での割り算は行えません。')
except TypeError as e:  
    print(e)  
    print('文字列と数値は連結できません。')
except ValueError as e:  
    print(e)  
    print('型変換が不正です。')

