# 10. В массиве хранится информация о количестве людей,
# живущих на каждом из 15 этажей дома
# (на первом этаже — в нулевом элементе массива, на втором — в первом и т. д.).
# Определить два этажа, на которых проживает меньше всего людей.
# (Если минимальное количество жителей одинаково на 2х и более этажах, то вывести наименьшие этажи).
import random

sp = [random.randint(6, 20) for i in range(15)]
min1 = min(sp)
print(sp)
temp = sp.copy()
temp.remove(min1)
min2 = min(temp)
print(sp.index(min1) + 1)
print(temp.index(min2) + 2 if temp.index(min2) >= sp.index(min1) else temp.index(min2) + 1)