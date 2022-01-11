import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#словарь программы
print("код взят из источника: https://codeby.net/threads/pishem-prostoj-generator-slozhnyx-parolej.64810/")
print("Простой консольный генератор паролей!\nДобро пожаловать")
number = input("Введите число паролей: " + "\n")
#число выводимых паролей
length = input("Введите длину пароля: " + "\n")
#длина выводимого пароля
number = int(number)
length = int(length)
print("Список сгенерированных паролей:" + "\n")
for n in range (number):
    password = ''
    for i in range (length):
        password += random.choice(chars)
    print(password)
#цикл случайной генерации паролей
input()
