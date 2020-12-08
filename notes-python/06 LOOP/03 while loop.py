'''
The break Statement
With the break statement we can stop the loop even if the while condition is true:
'''
i = 0
while i < 6:
    i += 1
    print(i)
    if i == 3:
        break #STOP the LOOP
#1
#2
#3
#下面結果一樣
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
#1
#2
#3

'''
iteration
noun [ C or U ]
UK  /ˌɪt.ərˈeɪ.ʃən/ US  /ˌɪt̬.əˈreɪ.ʃən/
 
formal
the process of doing something again and again, usually to improve it, or one of the times you do it
反覆（通常為了作出改善而重複做某事）
the repetition and iteration that goes on in designing something
在設計某物時的重複與反覆修改
The software is on its fifth iteration.
這個軟體已經是第五版。
'''

'''
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:
'''
print("--continue--")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue #繼續ＬＯＯＰ下一個 前面沒有指令所以i = 3時甚麼都沒做，也就是因為為什麼三沒有印出來
    print(i)
#1
#2
#4
#5
#6
print("--continue-2-")
i = 0
while i < 6:
    i += 1
    if i == 3:
        print(i*100)
        continue
    print(i)

#1
#2
#300
#4
#5
#6
'''
The else Statement

With the else statement we can run a block of code once when the condition no longer is true:

'''
print("while loop with else statement")
i = 1
while i < 6:    
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

