# 11. Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером).
import random

sp = [random.randint(1, 100) for i in range(10)]
print(sp)
it = 0
for i in range(len(sp)):
    if i != 0:
        if sp[i] > sp[i - 1]:
            it += 1
print(it)
