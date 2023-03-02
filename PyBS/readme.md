# Программа для записи видео с экрана на Python
![image](https://user-images.githubusercontent.com/86486142/222078881-13791861-aaee-409c-9ea7-d433c202ebdd.png)

Была сделана по [видео](https://youtu.be/UR32YTGAMHo) и немного модифицирована
- разрешение экрана программа определяет автоматически
- имя файла программа получает от юзера
- работает и на винде и на линуксе

[Запись экрана с помощью программы](https://disk.yandex.ru/i/e8fxhckDnSX93g)

# Код программы
Импортируем все необходимые модули (opencv, pyautogui, tkinter и numpy)
```Python
import cv2
import numpy as np
import pyautogui
import tkinter as tk
```
Измерение разрешения экрана при помощи tkinter (появившееся окно можно закрыть)
![image](https://user-images.githubusercontent.com/86486142/222422060-fd411c64-8fa4-4d1a-bce0-1e0fd7705922.png)
```Python
root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
```
Ввод названия видео (без расширения, по умолчанию *.avi)
![image](https://user-images.githubusercontent.com/86486142/222422239-f8b4afef-cc9c-4165-957b-1da911ca5a06.png)
```Python
video_name = input("Введите название видео: ")
```
Размер записываемой области (берется из ширины и высоты монитора пользователя)
```Python
SCREEN_SIZE = (width, height)
```
Обнаружение кодека на устройстве
```Python
fourcc = cv2.VideoWriter_fourcc(*"XVID")
```
Параметры записываемого видео
```Python
out = cv2.VideoWriter(f"{video_name}.avi", fourcc, 20.0, (SCREEN_SIZE))
```
Выход из программы
(Нажать на q нужно именно в программе, консоль можно закрыть, либо погасить процесс, зажав комбинацию Ctrl-C)
```Python
print("Для выхода нажать 'q' . . .")
```
Запись экрана (создание большого количества скриншотов с высокой скоростью и объединение их в массив)
```Python
while True:
	img = pyautogui.screenshot()
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	out.write(frame)
	cv2.imshow("screenshot", frame)

	if cv2.waitKey(1) == ord("q"):
		break
```
Выход из программы и закрытие всех окон при завершении выполнения
```Python
cv2.destroyAllWindows()
out.release()
```
