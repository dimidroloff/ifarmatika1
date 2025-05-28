from math import sqrt
a = float(input("Введите число а: "))
x = -a
while x < a:
    if abs(x) < 4:
        it = sqrt(2 * (x ** 2) + 1)
    else:
        it = x - 0.6
    print(it)
    x += 0.1