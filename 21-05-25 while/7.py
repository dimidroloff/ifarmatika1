# 7. Игра «Отгадай число». Компьютер загадал число от 1 до 10 (сформировал его случайным
# образом). Спрашивать у пользователя число, пока он не отгадает его.
import random

kakashka = random.randint(1, 10)
# print(kakashka)
a = int(input("Угадайте число от 1 до 10: "))
while a != kakashka:
    a = int(input("Угадайте число от 1 до 10: "))
print("ВАААу, Вы угадали!!!! Умница! Горжусь тобой🎉🎉🌹💋")