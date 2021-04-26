def myfanction(a, b):
    if a > b:
        print("Успешно")
    elif a == b:
        print("Почти")
    elif a < b:
        print("Лузер")


myfanction(int(input("Введите число: ")), int(input("Введите число: ")))
