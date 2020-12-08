def recursion_while_loop(m):
    result = number  = 1
    #! #! result CANT be 0 coz starting 0 * 1 = 0 ---> 0 * 2 = 0 --->  0 * 3 = 0
    while m <= 1:
        print(f"recursion of {m} is {m}")
    while m >= number:
        result = result * number
        #print(str(result))  #! check line 12 ~ 17
        number = number + 1
    print(f"{m:,}階層值是{result:,}")
recursion_while_loop(6)
#1 * 1 = 1
#        1 * 2 = 2
#                 2 * 3 = 6
#                         6 * 4 = 24
#                                 24 * 5 = 120
#                                          120 * 6 = 720