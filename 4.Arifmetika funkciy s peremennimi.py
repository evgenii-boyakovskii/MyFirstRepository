def myfanction(a, b):
    print(a, "+", b, "=", a+b)
    print(a, "-", b, "=", a-b)
    print(a, "*", b, "=", a*b)
    if b:
        print(a, "/", b, "=", a/b)
    else:
        print("You cannot divide by zero!")


myfanction(int(input("Введите число: ")), int(input("Введите число: ")))
