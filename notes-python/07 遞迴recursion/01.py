def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print(tri_recursion(6))


# 1
# 3
# 6
# 10
# 15
# 21
# 21

6 + (6-5)
