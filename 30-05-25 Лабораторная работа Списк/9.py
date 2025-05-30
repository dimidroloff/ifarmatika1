# 9. Даны результаты тестирования некоторой группы людей. Определите количество людей, набравших максимальное число баллов.

import random

sp4 = [random.randint(0, 100) for i in range(25)]
print(sp4)
print(sp4.count(max(sp4)))