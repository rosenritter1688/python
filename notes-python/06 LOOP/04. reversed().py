
#! reversed() 
#!  因為如果每次LOOP刪除一個東西 LIST的INDEX 變動   假如刪掉第一個之後 本來的是在第二個位置的 會在下一次LOOP時變成第一個，這樣子想要刪除的東西會被刪掉 
my_list = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven"]
            10     9       8      7     6      5      4       3       2      1      0
for item in reversed(my_list):
    print(item)