from threading import Timer

def sayHello():
    print("Hello\n")

'''
for x in range(5):
    tx = Timer(10.0,sayHello)  #一秒後執行sayHello
    tx.start()                 #啟動定時器

    ##等完10秒鐘曾已上市等完10秒鐘曾

同下
'''    

for x in range(5):
    Timer(10.0,sayHello).start() 
    #Timer要大寫
          #十秒後執行sayHello
                        #.start.()啟動定時器
