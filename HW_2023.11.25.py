a = 75
b = int(input("Введите число от 1 до 100: "))
while b != a:
    if b == 0:
        break
    elif b > a:
        print("Загаданное число меньше")
        b = int(input("Введите число от 1 до 100: "))
    elif a > b:
        print("Загаданное число больше")
        b = int(input("Введите число от 1 до 100: "))
    else:
        print("Ошибка")
if b == 0:
    print("Игра завершена досрочно")
if b == a:
    print("Поздравляем, вы угадали число!")
