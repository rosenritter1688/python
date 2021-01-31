
"""
try / except 例外處理
主要目的是相容不同版本的pyton 語言
例如python 2 輸入函數名為raw_input()
    python 3 輸入函數名為inpuit()
程式預設傳回raw_input()
如果有錯誤表示用的是python 3
就會傳回input()
"""
def text_prompt():
    try:
        raw_input("pls enter >> ")
        print("u r using Python 2.x")
        return 
    except NameError as error_msg: 
        print(error_msg)
        input("pls enter >> ")
        print("The python that u use is python 3.x")
        return

text_prompt()
# pls enter >> jj
# The python that u use is python 3.x



