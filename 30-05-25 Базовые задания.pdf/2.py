# 2. Сформировать список из N случайных чисел из диапазона от -50 до 50. Вывести его на экран.
import random

n = int(input())
sp = []
for _ in range(n):
    sp.append(random.randint(-50, 50))

print(sp)