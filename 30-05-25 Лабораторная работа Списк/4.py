# 4. Сформировать список из N случайных чисел из диапазона [10; 1000]. Найти кол-во трёхзначных чисел.
import random

sp4 = [random.randint(10, 1000) for i in range(int(input("Введите кол-во4: ")))]
print(sp4)
it4 = 0
for j in sp4:
    if 99 < j < 1000:
        it4 += 1
print("трехзначных -", it4)