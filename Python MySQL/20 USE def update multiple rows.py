用 ** 來收集關鍵字引數

    如果混合使用「位置參數」與 args 以及 *kwargs，就必須按照這個順序來排列它們
    如同 args，其實不需要呼叫關鍵字參數 kwargs，這只是一種慣例


def 變數(**kwargs):                                                            # 使用兩個星號（**）來將「關鍵字引數群組化」
    print('引數名稱:', kwargs)

變數(參數名稱1='引數1', 參數名稱2='引數2', 參數名稱3='引數3')
引數名稱: {'引數名稱1: '引數1', '引數名稱2: '引數2', '引數名稱3: '引數3'}
