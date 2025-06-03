# 2.	Сформировать список из N случайных чисел из диапазона [-10, 10]. Вывести на экран весь массив
import random

li = list()
for i in range(int(input())):
    li.append(random.randint(-10, 10))
print(li)