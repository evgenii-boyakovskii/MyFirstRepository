try:
    a = int(input("Введите целое число: "))
    b = int(input("Введите целое число: "))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
except ZeroDivisionError as e:
    print("На ноль делить нельзя")



print('Type "Quit" for exit')
while True:
    try:
        sign = input('Выберите одну из операций:"+","-","/","*": ')
        if sign == "Quit":
            break
        if sign not in ("+", "-", "/", "*"):
            print("Введите одну из предложенных операций")
            continue
        a = float(input("a = "))
        b = float(input("b = "))
        if sign == "+":
            print(a + b)
        elif sign == "-":
            print(a - b)
        elif sign == "*":
            print(a * b)
        elif sign == "/":
            print(a / b)
    except ZeroDivisionError as ex:
        print("На ноль делить нельзя")
    except ValueError as e:
        print("Введите целое число: ")

