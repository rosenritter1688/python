

#? 學會python P.6-26
target = 13
guess_times = 1
#! while (1)、while (true)、while True:
#while True: #* 無限ループ
#while(1):   #* 無限ループ
#while(True):#* 無限ループ
    print(f'the numbe of your {guess_times} guesses')
    guess = int(input("pls enter the number that u wanna guess between1~100 => "))
    if target == guess:
        print("u got the right number")
        break # end the loop
    if guess > target:              #! dont use elif also can
        print("too big")
        guess_times += 1
    else:
        print("too small")
        guess_times += 1