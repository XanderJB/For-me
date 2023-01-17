# Составление чеков на Python
![изображение](https://user-images.githubusercontent.com/86486142/212754703-36b8d9d0-bacc-4633-ad7d-76b43671259f.png)<br>

## Шапка таблицы
```Python
name = "Наименование"
number = "Кол-во штук"
prices = "Цена (руб.)"
itog = "Итого (руб.)"
```
## Массив для добавления товаров
```Python
a_list = []
```

## Объявление текстового файла для сохранения данных
```Python
f = open('spisok.txt', 'w')
```

## Запись данных от пользователя в массив и сохранение их в текстовый файл
```Python
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
```
