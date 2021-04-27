try:
    a = int(input("Введите целое число: "))
    b = int(input("Введите целое число: "))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
except ZeroDivisionError as e:
    print("На ноль делить нельзя")

