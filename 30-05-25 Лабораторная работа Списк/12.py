# 12. Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов, у которых есть два соседних элемента и при этом они оба меньше данного.
import random

sp = [random.randint(1, 100) for i in range(10)]
print(sp)
it = 0
for i in range(len(sp)):
    if i != 0 and i != len(sp) - 1:
        if sp[i + 1] < sp[i] > sp[i - 1]:
            it += 1
print(it)
