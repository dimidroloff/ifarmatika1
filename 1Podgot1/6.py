# Найти длину окружности L и площадь круга S заданного радиуса R
from math import pi

r = int(float(input("Введите радиус: ").replace(",", ".").strip()))

print(f"Длина окружности = {pi * r * 2:.3f}")
print(f"Площадь круга = {pi * r ** 2:.3f}")
