tmp = None
year = None

def text_prompt(msg):
  try:                                  
                                        """
                                        try / except 例外處理
                                        主要目的是相容不同版本的pyton 語言
                                        例如python 2 輸入函數名為raw_input()
                                            python 3 輸入函數名為inpuit()
                                        程式預設傳回raw_input()
                                        如果有錯誤表示用的是python 3
                                        就會傳回input()
                                        """
    return input(msg)
  except NameError:
    return input(msg)
