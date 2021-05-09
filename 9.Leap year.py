# Так он високосный??

def year(x):
    if x % 4 != 0 or (x % 100 == 0 and x % 400 != 0):
        print("Невисокосный")
    else:
        print("Високосный")

year(int(input("Введите год: ") ))