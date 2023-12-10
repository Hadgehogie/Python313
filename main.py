# print("Hello World!")
# print("Привет")

# name = "Elena"  # инициализация переменной
# print("Hello, ", name)
# age = 20.4
# print(age)
# text = "Hello"
# print(text)
# print(text + str(age))
# print(type(age))  # int - 20, float - 2-.4
# print(type(text))  # str = "Hello"
# a = False  # True
# print(a)
# print(type(a))  # bool - True, False

# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))

# a, b, c = 1, "Hello", 9.02
# print(a)
# print(b)
# print(c)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# c = a  # 1
# a = b  # 2
# b = c  # 1
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print("\tстрока \nсимволов D:\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", ", s2, "!\t\t"
# # print(s1, ", ", s2, "!"
# b = s3 * 5
# print(b)

# print(6 + 2)
# print(6 - 2)
# print(6 / 2)  # 3.0
# print(6 * 2)  # 1.5
# print(6 / 4)  # 3
# print(6 // 2)  # 1
# print(6 // 4)
# print(6 ** 2)
# print(6 % 4)


# num = 10
# num += 5  # num = num + 5
# print(num)
#
# num -= 3  # num = num - 3
# print(num)

# num = 4325
# print("Исходящее число:", num)
# a = num % 10
# print(a)  # 5
# num //= 10
# print(num)  # 432
# b = num % 10
# print(b)  # 2
# num //= 10
# print(num)  # 43
# c = num % 10
# print(c)  # 3
# d = num // 10
# print(d)  # 4
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4325
# print("Исходящее число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# res += num // 10
# print(res)

# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)  # 23
# res = int(num1) + num2  # 5
# print(res)

# print(int(3.8))
# print(round(3.891, 2))
# print(type(round(3.891, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="---", end="\n\n")
# print("Я учу Python.")

# name = input("Введите имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = input("Введите степень: ")
# res = num ** int(power)
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# False => "", 0, False

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 < 5)
# print(9 >= 9)
# print(5 <= 5)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)  # True && True => True
# print(2 * 5 > 7 >= 4 + 3)  # True && True => True
# print(3 * 3 <= 7 >= 2)  # True && False => False
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True: True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True: False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False: True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False: False)
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True: True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True: False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False: True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False: False)

# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 15
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ на сайт запрещен")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
# if (a > b + c) or (b > a + c) or (c > a + b):
#     print("Такого треугольника не существует")
# elif a == b == c:
#     print("Треугольник равносторонний")
# elif (a == b) or (b == c) or (a == c):
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Рабочий день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     elif n == 0:
#         n = "нет"
#         print(n, "ворон")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# password = "user"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'четверг'
# time = 13
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня не существует")

# a, b = 10, 20
#
# print(a if a < b else b)
#
# if a < b:
#     print(a)
# else:
#     print(b)

# a, b = 20, 30
#
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 10, 0
#
# print("На ноль делить нельзя" if b == 0 else a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n + 2)
# except:
#     print("Что-то пошло не так")
#
# print("Следующая строка")

# n = input("")
# m = input("")
# try:
#     n = int(n)  # n = 5
#     m = int(m)  # m = 'two'
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)  # '5' + 'two'

# i = int(input(""))
# n = int(input(""))
# while i < n:
#     i += 1
# print("*\n" * n)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a
#     a += 1
# print("Сумма нечетных чисел в пределах диапазона:1", res)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# if a % 2 == 0:
#     a += 1
# res = 0
# while a <= b:
#     # print("a =", a)
#     res += a
#     a += 2
# print("Сумма нечетных чисел в пределах диапазона:", res)


# ЦИКЛ FOR:
# for i in range(3):  # 0 1 2
#     print("+++ i =", i)
#     for j in range(2):  # 0 1
#         print("----- j = ", j)

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите длину прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

# СПИСКИ (АЛЯ МАССИВЫ):
# nums = [letter * 2 for letter in "Banana"]
# print(nums)

# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)

# Список (list)
# nums = [8, 5, 38, ":)", 90, 2, -8, ";)", 645, 12, 67]
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[2])
# print(nums[-4])
#
# nums[1] = 256
# print(nums)
# nums[4] += 100
# print(nums)

# nums = [8, 5, 38, ":)", 90, 2, -8, ";)", 645, 12, 67]
# print(nums)
# print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2)

# s = []
# print(s)
#
# b = list(["Hello", "World"])  # "Hello" => []
# print(b)
# print(b[0])

# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 10)))
# print(list(range(2, 10 + 1, 2)))

# [выражение for переменная in последовательность]

# a = [0 for _ in range(5)]
# print(a)
#
# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Ведите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# res = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print('Сумма отрицательных чисел: ', res)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# j = 0
# for i in a:
#     if i < 0:
#         j += 1
# print(j)

# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):  # 0 1 2 3 4 5 6 7 8
#     print(a[i] + 2, end=" ")  # a[i] = 10 20 30 40 50 60 70 80 90
#     print()
#
# for i in a:
#     print(i + 2, end=" ")  # 10 20 30 40 50 60 70 80 90

# n = int(input('Введите количество элементов списка: '))
# a = [int(input('-> ')) for _ in range(n)]

# sum_negative = sum([num for num in a if num < 0])
# print("Сумма отрицательных элементов: ", sum_negative)

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print('Сумма отрицательных элементов: ', sum([num for num in a if num < 0]))

# n = list(range(21, 41))
# print(n)
# odd = even = 0
#
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         even += 1
# #     else:
# #         odd += n[i]
#
# # for i in n:
# #     if i % 2 == 0:
# #         even += 1
# #     else:
# #         odd += i
#
# print("Количество четных элементов списка:", even)
# print("Сумма нечетных элементов списка:", odd)

# n = list(range(21, 41))
# print(n)
# a = 2
# print(n[a])
# print(n[a - 1])
# print(n[a + 1])

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print(a)
# for i in range(1, len(a)):
#     # print(a[i], "-> ", end="")
#     # print(a[i - 1])
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

# for i in a:
#     if i > i - 1:
#         print(i, end="")


# a = [1, 2, 3]
# b = a.copy()  # копирует список а
# print("a =", a)
# print("b =", b)
# a.append(20)
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)

# a = [5, 4, 1, 2, 3]
# print(a)
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)
#
# # a.sort()  # сортировка элементов списка
# # print(a)
# a.sort(reverse=True)
# print(a)

# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
#
# sort = sorted(a)
# print(sort)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(0, 9))  # от 3 до 9 включительно
# print(random.randrange(3, 9, 2))  # от 3 до 9 выколото
#
# print(random.uniform(10.5, 25.5))  # включительно; обязательно вещественное число
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ["Москва", "Новосибирск", "Санкт-Петербург", "Воронеж", "Омск"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
#
# s = [55, 66, 77, 88, 99]
# # print(random.choice(s))
# print(random.choices(s, k=5))
# random.shuffle(city_list)
# print(city_list)

# lst = [5, 4, 3, 2, 1]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# a = ['5', '4', '3', '2', '1']
# res = 0
# for i in a:
#     res += i
# print(sum(a))

# a = 5
#
# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sum(s))

# import random
# mas = [i for i in range(10)]
# print(mas)

# import random
# arr = [random.randint(0, 100) for i in range(10)]
# print(arr)
# print("Max:", max(arr))
# a = max(arr)
# arr.remove(a)
# arr.insert(0, a)
# print(arr)

# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print("Min:", min_ch)
#
# ind_min = lst.index(min_ch)
# print("Index min:", ind_min)
#
# # del lst[0: ind_min]
#
# print(lst[ind_min:])

# lst = [5]
# print(bool(lst))
# # # if len(lst) == 0:
# # if not lst:
# #     print("Список пуст")
# # else:
# #     print("В списке есть элементы")
# if lst:
#     print("В списке есть элементы")
# else:
#     print("Список пустой")

# import random
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for i in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
#
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print("Элементы обоих списков без повторений:", d)
#
# # c = []
# # x = [i for i in c if c.count(i) == 2]
# # print(x)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# m = ["Hello", "World"]

# print(m)
# print(len(m))
# print(m[1][2])
# print()
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# import random
# w, h = 4, 3
# matrix = [[random.randint(-20, 30) for x in range(w)] for y in range(h)]
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             m += 1
#     print()
# print("Количество отрицательных элементов:", m)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# w, h = 4, 3
# matrix = [[input("->") for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# # import math as m
# from math import *
# num1 = sqrt(1225)
# num2 = ceil(3.1)
# # num3 = m.floor(3.8)
# print(num1)
# print(num2)
# # print(num3)
# # print(m.pi)

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# seconds = time.time()
# print("Количество секунд:", seconds)
#
# locale_time = time.ctime()
# print("Местное время:", locale_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep='')
#
# print(time.strftime("Сегодня: %B %d, %Y"))
#
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime()))
#
# start = time.time()
# time.sleep(1020)
# finish = time.time()
# res = finish - start
# print(res)


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# n1 = 1
# n2 = 5
# n4 = 2
# print(get_sum(n1, n2, d=n4))

# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, "*")
# set_param(s="#")

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")  # TypeError

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False

# a = 'Hello'
# b = 'Hello'
# print(id(a))
# print(id(b))
# print(a == b)  # True
# print(a is b)  # True

# n = 5
# m = 5
# print(id(n))
# print(id(m))
# print(n == m)  # True
# print(n is m)  # True

# n = [1, 2, 3]
# print(id(n))
#
# n.append(4)
# print(n)
# print(id(n))


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1
# print(ptl1)

countries =(
    ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
    ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
)
print(countries, end='\n\n')

for country in countries:
    country_name, country_population, cities = country
    print("\nСтрана:", country_name + ",", "Население =", country_population)
    for city in cities:
        city_name, city_population = city
        print("\nГород:", city_name + ",", "Население =", city_population)
