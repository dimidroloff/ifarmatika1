# 7. Определить, есть ли в строке две подряд гласные буквы
a = input()
gl = "уеыаоэяиюё"
fl = False
for i in range(len(a)):
    if i != len(a) - 1 and a[i] in gl and a[i + 1] in gl:
        print(a[i], a[i + 1])
        fl = True

if fl:
    print("да есть гласные подряд")
    # Абра Кадабра Абра унананаа Абраа у гагаааа
else:
    print("Нету")
    # Абра Кадабра Абра унанана Абра у гага

