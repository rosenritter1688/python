
#*  0、empty string、empty list、empty tuple are  #! FASLE
#*  others are True

#* even list [0]、 tuple (0) are TRUE too


#* 結合and , or , not組成更長的邏輯計算時，需要注意"短路"行為一旦計算式已經得知結果，就不會再繼續運算


list0 = [ ]
list1 = [30,41,52]
print(list0 and list0[0] > 25)   #! 光看list[0]