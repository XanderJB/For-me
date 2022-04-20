def __init__(self):
    pass

class Length:
    @classmethod
    def length(self):
        while True:
            metr = int(input("Введите длину объекта в м: "))
            choise_2 = int(input("В какую меру длины вы хотите преобразовать?\n1 - км\n2 - дм\n3 - см\n4 - мм\n"))
            if choise_2 == 1:
                km = metr / 1000
                print(f"Результат равен {km} км")
            elif choise_2 == 2:
                dm = metr * 10
                print(f"Результат равен {dm} дм")
            elif choise_2 == 3:
                sm = metr * 100
                print(f"Результат равен {sm} см")
            elif choise_2 == 4:
                mm = metr * 1000
                print(f"Результат равен {mm} мм")
            else:
                print("Команда не распознана")
            q = input("Введите q, чтобы выйти: ")
            if q == "q":
                break
class Area:
    @classmethod
    def area(self):
        while True:
            sqm = int(input("Введите площадь объекта в м²: "))
            choise = int(input("В какую меру площади вы хотите преобразовать?\n1 - км²\n2 - дм²\n3 - см²\n4 - га\n"))
            if choise == 1:
                sqkm = sqm / 1000000
                print(f"Результат равен {sqkm} км²")
            elif choise == 2:
                sqdm = sqm * 100
                print(f"Результат равен {sqdm} дм²")
            elif choise == 3:
                sqsm = sqm * 10000
                print(f"Результат равен {sqsm} см²")
            elif choise == 4:
                ga = sqm / 10000
                print(f"Результат равен {ga} га")
            else:
                print("Команда не распознана")
            q = input("Введите q, чтобы выйти: ")
            if q == "q":
                break

class Volume:
    @classmethod
    def volume(self):
        while True:
            сm = int(input("Введите объем объекта в м³: "))
            choise = int(input("В какую меру объема вы хотите преобразовать?\n1 - дм³\n2 - см³\n3 - л\n"))
            if choise == 1:
                сdm = сm * 1000
                print(f"Результат равен {сdm} дм³")
            elif choise == 2:
                сsm = сm * 1000000
                print(f"Результат равен {сsm} см³")
            elif choise == 3:
                l = сm * 1000
                print(f"Результат равен {l} л")
            elif choise == 4:
                ml = сm * 1000000
                print(f"Результат равен {ml} мл")
            else:
                print("Команда не распознана")
            q = input("Введите q, чтобы выйти: ")
            if q == "q":
                break

class Weight:
    @classmethod
    def weight(self):
        while True:
            kg = int(input("Введите массу объекта в кг: "))
            choise = int(input("В какую меру массы вы хотите преобразовать?\n1 - т\n2 - ц\n3 - г\n4 - мг\n"))
            if choise == 1:
                t = kg / 1000
                print(f"Результат равен {t} т")
            elif choise == 2:
                c = kg / 100
                print(f"Результат равен {c} ц")
            elif choise == 3:
                g = kg * 1000
                print(f"Результат равен {g} г")
            elif choise == 4:
                mg = kg * 1000000
                print(f"Результат равен {mg} мг")
            else:
                print("Команда не распознана")
            q = input("Введите q, чтобы выйти: ")
            if q == "q":
                break