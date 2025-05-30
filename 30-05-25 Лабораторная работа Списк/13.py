# 13. Даны два массива чисел.
# Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
import random

sp = [random.randint(1, 100) for i in range(10)]
sp2 = [random.randint(1, 100) for j in range(10)]
print(sp, sp2, sep="\n")
pr = 0
for i in sp:
    if i not in sp2:
        print(i, end=" ")
    else:
        pr += 1
print("\nПропусков -", pr)