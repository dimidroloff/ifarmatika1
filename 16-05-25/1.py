# Дано 3 числа. Найти минимальное среди них и вывести на экран.
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

print("минимальное число:", min(a, b, c))
if a < b <= c or a < c <= b:
    print(a)
elif b < a <= c or b < c <= a:
    print(b)
else:
    print(c)