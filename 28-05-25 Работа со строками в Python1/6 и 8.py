# 6. В тексте заменить цифры на их словесные названия
# Исходный текст набран с ошибками:
# между некоторыми словами по несколько пробелов.
# Заменить в тексте подряд идущие пробелы одним пробелом.
import num2words
a = input()
it = []
for i in a.split():
    try:
        temp = int(i)
        slovo = num2words.num2words(temp, lang="ru")
        it.append(slovo)
    except Exception:
        it.append(i)
print(" ".join(it))

# Сегодня    234   раза я  моргнул