# Треугольник задан координатами своих вершин. Найти периметр и площадь треугольника
import math
a = input("Введите первые координаты (вид - x, y): ")
x1 = int(a.split(", ")[0])
y1 = int(a.split(", ")[1])
b = input("Введите вторые координаты: ")
x2 = int(b.split(", ")[0])
y2 = int(b.split(", ")[1])
c = input("Введите третьи координаты: ")
x3 = int(c.split(", ")[0])
y3 = int(c.split(", ")[1])
print(x1, y1, x2, y2, x3, y3)

ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(ab)
bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
print(bc)
ac = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
print(ac)
p = sum((ab, bc, ac)) / 2

print(f"Периметр = {p}")
print(f"Площадь = {1 / 4 * math.sqrt(p * (p - ab) * (p - bc) * (p - ac))}")