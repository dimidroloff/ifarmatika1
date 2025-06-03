# 1.Сформировать список из 15 чисел, вводимых с клавиатуры.  Вывести весь массив.  Ввести число x, определить его индекс в массиве.  (25 баллов)

li = list()
for i in range(0, 15):
    a = int(input(f"{i}: "))
    li.append(a)

x = int(input("X: "))
if x in li:
    print(li.index(x))
else:
    print("Такого нет")