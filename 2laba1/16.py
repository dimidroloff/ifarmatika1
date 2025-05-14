# Получить случайное четырёхзначное целое число и вывести через запятую его отдельные
# цифры.
from random import randint
a = str(randint(1000, 9999))
print("Число:", a)
print("Цифры: ", end="")
for i in a:
    print(i, end=", ")