'''
https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-11ed5d300d3d

在解決問題時，我們經常會遇到無法輕鬆使用 loop 或是 if statement就能處理的問題，
像是走迷宮問題遇到死路時需要回到上一層計算、或是在解決河內塔問題時儘管操作相同，
卻因為每次要進行操作的參數不同而需要寫重複的程式碼等等。
此時，一個經常被納入考慮的方法，就是利用遞迴的概念來撰寫一個函式。

重點
>>將一個大問題拆解成重複眾多小問題
>>自我呼叫和終結條件
>>經典例子:階乘、費氏數列、最大公因數

在數學以及電腦科學的領域當中，當一個函式會在執行當中，會不斷地自己呼叫自己時，
我們便認為這個函式具有遞迴的性質。同時，
#! 為了避免函式永無止盡地自我呼叫 (self-calling)，我們也需要設計一個明確的終止條件。
因此，我們便得到了設計一個遞迴函式的兩個重點：遞迴自我呼叫的方式以及結束呼叫的終止條件
'''
'''
階乘關係圖
factorial(4)
=   4 * factorial(3)            #= 4*3!  #分成PART4
    =   3 * factorial(2)        #= 3*2!  #分成PART3
        =   2 * factorial(1)    #= 2*1!  #分成PART2
            =   1                        #分成PART1   
                                         part1處理完再做part2以此類推
'''

def factorial(n):
    if n == 0 or n == 1:  #如果n輸入的是1 or 0停止遞迴並回傳n
        return n
    else:
        return n * factorial(n - 1)#遞迴(呼叫自己)
#print(factorial(6))

'''
W3School example
'''





# # Recursion Example Results
# # 1
# # 3
# # 6
# # 10
# # 15
# # 21

''' #! its a working code

m = int(input("請輸入要算的階層值 "))
number = result = 1
#number = 1
#result = 1
#! result CANT be 0 coz starting 0 * 1 = 0 ---> 0 * 2 = 0 --->  0 * 3 = 0
while number <= m:
    result = result * number
    number = number + 1
print(f"{m:,}階層值是{result:,}")
'''


#m階層 = 6
#number = 1
#result = 1
#result = result * number
#number = num


#1 * 1 = 1
#        1 * 2 = 2
#                 2 * 3 = 6
#                         6 * 4 = 24
#                                 24 * 5 = 120
#                                          120 * 6 = 720


'''#! its a working code
def recursion_while_loop(m):
    result = number  = 1
    while m <= 1:
        print(f"recursion of {m} is {m}")
    while m >= number:
        result = result * number
        number = number + 1
    print(f"{m:,}階層值是{result:,}")
recursion_while_loop(6)
'''