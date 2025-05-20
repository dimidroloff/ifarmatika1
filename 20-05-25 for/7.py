# 7. Найти сумму чисел от a до b (вводятся с клавиатуры)
s = 0
for i in range(int(input()), int(input()) + 1):
    s += i

print(s)