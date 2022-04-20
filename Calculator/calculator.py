import conv
from conv import *

def calc():
    while True:
        a = int(input("Введите 1-е число: "))
        b = int(input("Введите 2-е число: "))
        res = input("Выберите действие: \n1 - сложение; \n2 - вычитание; \n3 - умножение; \n4 - деление.\n")
        try :
            (res == a // b)
        except ZeroDivisionError :
            print("Делить на 0 нельзя!\nОстановка выполнения программы")
            break
        def multi_num(res):
            if res == '1':
                return a + b
            if res == '2':
                return a - b
            if res == '3':
                return a * b
            if res == '4':
                return a // b; a/b
            #raise ValueError('Неизвестный оператор {}'.format.res)
        print(multi_num(res))
        exit = input("Введите q, чтобы выйти. \nНажмите Enter, чтобы продолжить использовать Калькулятор: ")
        if exit == "q":
            break
    input("Нажмите любую клавишу, чтобы выйти...")
def volume():
    num_1 = float(input("Введите длину(м3): "))
    num_2 = float(input("Введите ширину(м3): "))
    num_3 = float(input("Введите высоту:(м3) "))
    res = num_1*num_2*num_3
    print(f"Объем фигуры равен: {res} кубометров")

choise = int(input("Добро пожаловать\nЧто вы хотите посчитать?\n1 - просто цифры\n2 - объем фигуры\n3 - конвертер\n"))
if choise == 1:
    calc()
elif choise == 2:
    volume()
elif choise == 3:
    a = int(input("Выберите меру длины\n1 - длина\n2 - площадь\n3 - объем\n4 - масса\n"))
    c = conv
    if a == 1:
        c.Length.length()
    elif a == 2:
         c.Area.area()
    elif a == 3:
         c.Volume.volume()
    elif a == 4:
         c.Weight.weight()
    else:
        print("Команда не распознана")
else:
    print("Вы ничего не выбрали")

