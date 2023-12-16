fig = int(input("Выберите фигуру (1 - прямоугольник; 2 - треугольник; 3 - круг): "))
if fig == 1:
    a = int(input("Длина: "))
    b = int(input("Ширина: "))
    print("Площадь:", a * b)
elif fig == 2:
    a = int(input("Основание: "))
    h = int(input("Высота: "))
    print("Площадь:", a * h / 2)
elif fig == 3:
    import math as m
    r = int(input("Радиус: "))
    S = round(m.pi * (r ** 2), 2)
    print("Площадь:", S)
