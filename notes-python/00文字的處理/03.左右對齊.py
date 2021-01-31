
#! .ljsut 向左靠齊  .rjust 向右靠齊
string_a = "kok"
int_a = 1234  
print(string_a,int_a)
##ok 1234
print(string_a.ljust(10)+str(int_a).rjust(10))
##ok             1234
print(f"{string_a.ljust(10):_^20},{str(int_a).rjust(10):~^20}")
#_____kok       _____,~~~~~      1234~~~~~