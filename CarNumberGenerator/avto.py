import random

words = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
region = [102, 113, 116, 121, 123, 124, 125, 136, 142, 150, 190, 152, 154, 159, 161, 163, 164, 173, 174, 177, 199, 197, 777, 178]

for i in range(1, 10):
    region.append("0" + str(i))

for q in range(10, 100):
    region.append(q)

region.remove(20)

number_reg = int(input("Сколько номеров сгенерировать: "))
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