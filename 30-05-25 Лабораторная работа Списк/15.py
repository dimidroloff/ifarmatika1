# 15. Дан массив чисел. Необходимо выбрать в другой массив все элементы исходного массива, которые встречаются более одного раза.

import random

sp = [random.randint(1, 100) for i in range(10)]
print(sp)
pr = []

for i in sp:
    if sp.count(i) > 1:
        if i not in pr:
            pr.append(i)

if pr:
    print(pr)
else:
    print(0)
