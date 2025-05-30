# 7. Сформировать список из N случайных чисел из диапазона [-10; 10]. Найти максимальный элемент списка.
import random

sp4 = [random.randint(-10, 10) for i in range(int(input("Введите кол-во: ")))]
print(sp4)
print(max(sp4))