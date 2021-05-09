# Сравним списки?

from random import randint


def myfunction(a, b, c):
    x1 = [randint(b, c) for _ in range(a)]
    x2 = [randint(b, c) for _ in range(a)]
    if x1 == x2:
        print("Все совпало!")
    else:
        result = list(set(x1) ^ set(x2))
        print(result, " - уникальные числа!")


myfunction(int(input("Введите нужное количество чисел: ")), int(input("Введите нижнюю границу: ")),
           int(input("Введите верхнюю границу: ")))
