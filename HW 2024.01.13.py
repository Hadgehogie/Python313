import math
from math import *

print('Площадь окружности с радиусом 4:', (lambda r: (r ** 2) * math.pi)(4))
print('Площадь прямоугольника 13х25:', (lambda x, y: x * y)(13, 25))
print('Площадь треугольника с основанием 12 и высотой 4:', (lambda a, h: a * h / 2)(12, 4))

