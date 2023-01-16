# Составление чека на Python
name = "Наименование"
number = "Кол-во штук"
prices = "Цена (руб.)"
itog = "Итого (руб.)"

a_list = []
f = open('spisok.txt', 'w')
while True:
    product_name = input("Введите наименование товара: ")
    num = int(input("Введите количество товара: "))
    price = int(input("Введите стоимость товара: "))
    
    a_list.append(f"{product_name:<20}|{num:^20}|{price:^20}|{price*num:^20}")
 
    print("="*30)
    exit = input("Хотите выйти?(y/N): ")
    
    if exit == "y" or exit == "н":
        break

f.write(f"|{name:<20}|{number:^20}|{prices:^20}|{itog:^20}|")
for i in a_list:
   f.write(f"|{i}|")
    

# a_list = []
# while True:
    # a, b, c = map(str, input().split())
    # a_list.append(f"{a}, {b}, {c}")
    # e = input("Exit?(y/n): ")
    # if e == "y":
        # break
# for i in a_list:        
    # print(i)