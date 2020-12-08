

#? 學會python P.6-28 
result = 0
for a in range(1,101):
    if 39 < a < 68:
        print(a)
        result +=a
        print(f"sum of a = {result}")
print(result)