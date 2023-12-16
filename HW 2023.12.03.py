import random

num = int(input("Размер списка: "))
arr = [random.randint(0, num - 1) for i in range(100)]
res = []
for element in arr:
    if element not in res:
        res.append(element)
print(arr)
print(res)
