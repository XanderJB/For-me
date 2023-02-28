import cv2
import numpy as np
import pyautogui
from datetime import datetime
import tkinter as tk

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

video_name = input("Введите название видео: ")

SCREEN_SIZE = (width, height)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter(f"{video_name}.avi", fourcc, 20.0, (SCREEN_SIZE))
print("Для выхода нажать 'q' . . .")

while True:
	img = pyautogui.screenshot()
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	out.write(frame)
	cv2.imshow("screenshot", frame)

	if cv2.waitKey(1) == ord("q"):
		break

cv2.destroyAllWindows()
out.release()
