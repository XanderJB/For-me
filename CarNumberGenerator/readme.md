# Простой генератор автомобильных номеров
![image](https://user-images.githubusercontent.com/86486142/222418606-f22cd96e-2fac-4684-99af-8ccb8685c6cd.png)
# Код генератора
Импортируем модуль random
```Python
import random
```
Создаем три списка с буквами, цифрами и номерами регионов
```Python
words = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
region = [102, 113, 116, 121, 123, 124, 125, 136, 142, 150, 190, 152, 154, 159, 161, 163, 164, 173, 174, 177, 199, 197, 777, 178]
```
Добавляем через цикл for недостающие номера регионов и убираем регион 20, ибо он заменен на 95
```Python
for i in range(1, 10):
    region.append("0" + str(i))

for q in range(10, 100):
    region.append(q)

region.remove(20)
```
Спрашиваем у пользователя, сколько номеров сгенерировать?
```Python
number_reg = int(input("Сколько номеров сгенерировать: "))
```
Генерация случайных номеров
```Python
for i in range(0, number_reg):
    a = random.choice(words)
    b = random.choice(words)
    c = random.choice(words)

    d = random.choice(nums)
    e = random.choice(nums)
    f = random.choice(nums)

    r = random.choice(region)

    i = f"|{a}{d}{e}{f}{b}{c}|{r} RUS|"
    print(i)
```
