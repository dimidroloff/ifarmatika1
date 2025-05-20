# 6. Вывести на экран все нечетные числа от n до 1 (n>=1).
for i in range(int(input()), 0, -1):
    if i % 2 != 0:
        print(i)