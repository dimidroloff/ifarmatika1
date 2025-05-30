# 1. В программе задан список из 10 чисел с конкретными значениями из диапазона от 1 до 100
# (задается программистом непосредственно в программе перечислением чисел).

sp = [1, 3, 7, 33, 66, 77, 88, 99, 3, 42]
# 1.1. Вывести на экран пятый элемент списка.
print(sp[5])
# 1.2. Вывести на экран элементы списка с третьего по седьмой.
print(sp[3:7])
# 1.3. Вывести на экран элементы списка с нулевого по седьмой.
print(sp[:7])
# 1.4. Вывести на экран элементы списка с пятого по последний.
print(sp[5:])
# 1.5. Вывести на экран четыре последних элемента.
print(sp[-4:])
# 1.6. Вывести на экран элементы списка, стоящие на четных местах (нулевое место будем
# считать четным).
print(sp[::2])
# 1.7. Вывести на экран последний элемент списка двумя способами.
print(sp[-1])
print(sp[9])
# 1.8. Вывести на экран элементы списка в обратном порядке.
print(sp[::-1])
# 1.9. Вывести на экран три последних элемента в обратном порядке, то есть сначала
# последний, затем предпоследний и затем третий с конца.
print(sp[:-4:-1])
# 1.10. Найти минимальное и максимальное число в списке.
print(min(sp), max(sp))
# 1.11. Вывести индексы минимального и максимального элементов.
print(sp.index(min(sp)), sp.index(max(sp)))
# 1.12. Запросить у пользователя число. Есть ли оно в списке?
# 1.13. Запросить у пользователя число. На каком месте стоит это число? Если такого числа нет,
# то вывести сообщение об этом.
a = int(input())
if a in sp:
    print("Да, есть в списке🎢")
    print(f"Это число на {sp.index(a) + 1} месте")
    # 1.14. Сколько таких чисел в списке?
    print(f"Таких чисел в скиске - {sp.count(a)}")
else:
    print("Нет, нету в списке 🐱‍🐉🐱‍🐉🤷‍♂️")

# 1.15. Заменить третий элемент на число 555.
print()
print(sp)
sp[3] = 555
print(sp)
# 1.16. Добавить число 777 в конец списка.
sp.append(777)
print(sp)
# 1.17. Добавить число 333 на 8 место.
sp.insert(8, 333)
print(sp)
# 1.18. Удалить второй элемент списка.
sp.pop(2)
print(sp)
# 1.19. Удалить из списка числа 33 и 55, если они есть.
if 33 in sp:
    sp.remove(33)
if 55 in sp:
    sp.remove(55)
print(sp)
