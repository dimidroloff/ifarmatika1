# Вариант 14. Рейтинг бакалавра заочного отделения при поступлении в
# магистратуру определяется средним баллом по диплому, умноженным на
# коэффициент стажа работы по специальности, который равен:
# нет стажа - 1,
# меньше 2 лет - 13,
# от 2 до 5 лет - 16.
# Составить программу расчета
# рейтинга при заданном среднем балле диплома (от 3 до 5) и вывести
# сообщение о приеме в магистратуру при проходном балле 45.

a = float(input('ср балл диплома - ').replace(',', '.').strip())
b = float(input('стаж - ').replace(',', '.').strip())
k = 1

if b <= 0:
    k = 1
elif b < 2:
    k = 13
elif b < 5:
    k = 16
else:
    k = 1

it = a * k
print("ok" if it > 45 else "no")
