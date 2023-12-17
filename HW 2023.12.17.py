a = input("Введите строку: ")
check = set("аоуыэяёюие")
res = 0
for i in a:
    if i in check:
        res += 1
print(a)
print("Количество гласных:", res)
