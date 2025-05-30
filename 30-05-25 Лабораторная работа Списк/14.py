# 14. Дан массив чисел. Необходимо записать
# в другой массив все простые числа исходного массива.
# Если в исходном массиве нет простых чисел, программа должна вывести число 0.

import random

sp = [random.randint(1, 100) for i in range(10)]
print(sp)
pr = []

for i in sp:
    fl = True
    for j in range(i // 2 + 2):
        if j != 1 and j != 0 and j != i and i % j == 0:
            fl = False
            break
    if fl:
        pr.append(i)

if pr:
    print(pr)
else:
    print(0)