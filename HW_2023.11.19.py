am = int(input("Введите количество символов: "))
sym = input("Введите любой символ: ") + " "
print("0 - горизонтальная ориентация линии")
print("1 - вертикальная ориентация линии")
orient = int(input("Введите выбранную ориентацию линии: "))

show = 0
result = ""
if orient == 0:
    while show <= am:
        result += sym
        show += 1
    print(result)
elif orient == 1:
    while show <= am:
        print(sym)
        show += 1
else:
    print("Действие не может быть выполнено :(")
