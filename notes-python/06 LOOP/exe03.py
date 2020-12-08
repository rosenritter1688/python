

fold = 0
length = int(input("pls enter the length fo the rope in cm => "))

while True:
    length /= 2
    if length > 20:
        fold += 1
    else:
        fold += 1
        print(f'you must fold {fold} times so the rope will be less than 20 cm')
        break  #? without break will just keep looping
        