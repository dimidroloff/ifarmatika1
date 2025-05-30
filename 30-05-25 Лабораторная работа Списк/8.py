# 8. Сформировать список из N случайных чисел из диапазона [-10; 10]. Найти минимальный элемент списка. Сколько элементов списка равны минимальному?
import random

sp4 = [random.randint(-10, 10) for i in range(int(input("Введите кол-во: ")))]
print(sp4)
print(min(sp4))
print(sp4.count(min(sp4)))