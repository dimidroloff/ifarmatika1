# 13. Введите число k. Вычислить произведение чисел от 1 до k.
s = 1
for i in range(1, int(input()) + 1):
    s *= i

print(s)