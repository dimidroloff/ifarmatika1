# 2. Спрашивать у пользователя числа, пока он не введёт 0. Сколько чисел он ввёл (не считая
# нуля)?
a = input("Ввод: ")
n = 0
while a != "0":
    a = input("Ввод: ")
    n += 1
print(n)