# 3. Найти первое вхождение слово «Компьютер» в строку, введенную с клавиатуры.
# Если слова нет, то вывести на экран соответствующую надпись

a = input()
if a.lower().find("компьютер") != -1:
    print("Первое вхождение -", a.lower().find("компьютер"))
else:
    print("Нет вхождений")

# Ой май гад Компьютер