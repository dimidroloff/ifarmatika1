# 5. Сформировать список из N случайных чисел из диапазона [-10; 10]. Найти сумму положительных чисел.
import random

sp4 = [random.randint(-10, -10) for i in range(int(input("Введите кол-во: ")))]
print(sp4)
summ = 0
for j in sp4:
    if j >= 0:
        summ += j
print("Сумма положительных -", summ)