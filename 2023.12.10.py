a = [input("Введите числовые элементы кортежа подряд без пробелов: ")]
check = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
res = []
for i in a:
    res += i
res = tuple(res)
print(res)

no_dub = []
dub = []
for element in res:
    if element in check and element not in no_dub:
        quant = 0
        no_dub.append(element)
        quant += 1
        # for i in res:
        # if element in check and element in no_dub:
        #     quant += 1
        print("Количество " + element + ":", quant)
