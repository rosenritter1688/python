string_a = "みかん\nリンゴ\nバナナ\nパイナップル"

arr01 = string_a.splitlines()
print(arr01)

arr02 = string_a.splitlines(True)
print(arr02)

arr03 = string_a.splitlines(False)
print(arr03)