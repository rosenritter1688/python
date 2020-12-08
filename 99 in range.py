for x in range (1,10):
    for n in range(1,10):
        print("{} x {} = {:2}".format(x,n,x*n))


def my_function(n):
    """
    計算はここに置いといて
    """
    return print(n)
n = "hello"
my_function(n)
##hello
my_function("kk")
##kk


##use sticky 變大button 
btn = Button(win,)
btn.grid(row=1,column=1,sticky=W+E)



scale1 = Scale(win)
scale1.grid(row=1,column=1)