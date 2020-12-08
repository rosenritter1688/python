def factorial_loop (n):#這方式比遞迴(呼叫自己)快
    factor = 1
    for i in range(1,n+1):
        factor = factor * i
    return print(factor)
factorial_loop(6)
