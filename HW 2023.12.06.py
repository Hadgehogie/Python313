import random
arr = [random.randint(0, 10) for i in range(10)]
res = []
for element in arr:
    if element not in res:
        res.append(element)
print(arr)
print(res)
