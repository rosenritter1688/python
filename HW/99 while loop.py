i=0
while i < 9:
    i +=1
    d=0   #! without this will cause 1 * 1 ~ 1 * 9 only
    while d < 9:
        d += 1
        print("{} x {} = {:2}".format(i,d,d*i))
        #print("%d x %d = %d"%(d,i,d*i))
    