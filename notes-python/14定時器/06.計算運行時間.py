import time
factor = 0
def factorial_loop (n):#這方式比factorial()快
    global factor
    factor = 1
    for i in range(1,n+1):
        factor *= i
    return factor

def factorial(n):
    if n == 0 or n == 1:  #如果n輸入的是1 or 0停止遞迴並回傳n
        return n
    else:
        return n * factorial(n - 1)#遞迴(呼叫自己)

start_time = time.time()
factorial_loop(500)
end_time = time.time()
factorial_loop_timer = end_time - start_time
print(f'factorial_loop\'s Execution time: {end_time - start_time}')
#print(isinstance(factor,int))
#print(factorial_loop(10))
print("factorial_loop_timer is ",str(factorial_loop_timer))




start_time_2 = time.time()
factorial(500)
end_time_2 = time.time()
print(f'factorial\'s Execution time: {end_time_2 - start_time_2}')
factorial_timer =  end_time - start_time
print("factorial_timer is ",str(factorial_timer))
#print(factorial(1))

#print("hehehe",factorial(100))
if factorial_timer > factorial_loop_timer:
    print("factorial_loop is faster than factorial")
else:
    print("factorial is faster than factorial_loop")