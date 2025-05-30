# 6. Сформировать список из N случайных чисел из диапазона [1; 100]. Правда, что в списке чётных чисел больше, чем нечётных?
import random

sp4 = [random.randint(1, 100) for i in range(int(input("Введите кол-во: ")))]
print(sp4)
chet = 0
nechet = 0
for j in sp4:
    if j % 2 == 0:
        chet += 1
    else:
        nechet += 1
print("Да, чётных чисел больше, чем нечётных" if chet > nechet else "Нет, чётных чисел меньше, чем нечётных")