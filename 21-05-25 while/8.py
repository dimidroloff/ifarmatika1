#  8. Игра «Отгадай число». Компьютер загадал число от 1 до 20 (сформировал его случайным
# образом). Спрашивать у пользователя число, пока он не отгадает его. Каждый раз, когда
# пользователь не угадывает число, давать ему подсказку «Нет, моё число больше твоего»
# или «Нет, моё число меньше твоего».
import random

chisl = random.randint(1, 20)
a = int(input("Ввод: "))
while a != chisl:
    if a < chisl:
        print("Нет, моё число больше твоего")
    else:
        print("Нет, моё число меньше твоего")
    a = int(input("Ввод: "))
print("Ok")