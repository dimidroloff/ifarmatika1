# 3. Сформировать список из N чисел, введённых с клавиатуры, каждое число – на отдельной
# строчке. Вывести его на экран.

n = int(input())
sp = []
for _ in range(n):
    sp.append(int(input()))

print(sp)