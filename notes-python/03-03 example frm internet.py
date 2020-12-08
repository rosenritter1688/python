def text_prompt(msg):
    global n
    try:
        n = float(input(msg))  #! '請輸入身高值==>'    等於msg    #? 看不懂的話看下面的例子line 18~26
        return n
    except:
        print('你输入的类型错误！')

def get_BMI():
    h = text_prompt('請輸入身高值==>')
    w = text_prompt('請輸入體重值==>')
    BMI = w / (h * h)
    print('%f'%BMI)
get_BMI()
#? explanion see below


# def get_BMI():
#     global n
#     text_prompt('請輸入身高值==>')
#     h = n
#     text_prompt('請輸入體重值==>')
#     w = n
#     BMI = (w / (h * h)) * 10000
#     print('%f'%BMI)
# get_BMI()