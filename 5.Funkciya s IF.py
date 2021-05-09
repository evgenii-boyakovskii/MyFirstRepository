def myfunction(a, b):
    if a > b:
        print("Успешно")
    elif a == b:
        print("Почти")
    elif a < b:
        print("Лузер")


myfunction(int(input("Введите число: ")), int(input("Введите число: ")))
