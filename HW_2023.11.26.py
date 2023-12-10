# print("Найти среднее арифметическое всех ненулевых элементов введенного списка")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# up = 0
# down = 0
# for i in range(len(a)):
#     up += a[i]
#     if a[i] != 0:
#         down += 1
# print("Среднее арифметическое:", up / down)

a = [int(input("-> ")) for i in range(int(input("n = ")))]
for i in range (len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')
