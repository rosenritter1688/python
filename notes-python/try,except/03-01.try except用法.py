
#? try / except 例外處理
#! 我做的只是要輸入兩個之後才會傳回輸入錯誤看03-03的例子，對方式輸入錯一個就會跳出錯誤訊息
w = None
h = None
def error_input_check():
  global h,w,int_h,int_w
  try:
      int_h = int(h)
      int_w = int(w)
      if isinstance(int_h, int) == True and isinstance(int_w, int) == True:
        return int_h,int_w
  except:
      return False

def get_BMI():
  global h,w,int_h,int_w
  h = input('請輸入身高值==>')
  w = input('請輸入體重值==>')
  error_input_check()
  if error_input_check() == False:
    #print(error_input_check)
    print('你输入的类型错误！')
  else:
    BMI = int_w / ((int_h/100) * (int_h/100))
    print('%f'%BMI)
get_BMI()
