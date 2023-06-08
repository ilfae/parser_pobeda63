import os
from tkinter import *
import sys


# создаем функции для кнопок
def light_theme():
    root.withdraw()
    os.system('python run/custom.py')
    root.deiconify()
    root.destroy()

def dark_theme():
    root.withdraw()
    os.system('python run/custom_dark.py')
    root.deiconify()
    root.destroy()


# создаем главное окно приложения
root = Tk()
root.title("")
root.resizable(width=False, height=False) # запрещаем изменение размеров окна

# вычисляем координаты для центрирования окна
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 135
window_height = 50
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}") # задаем размер и координаты окна

root.iconbitmap('run/icon.ico')


# создаем кнопки
light_button = Button(root, text="Светлая", bg="white", fg="black", command=light_theme)
light_button.pack(side=LEFT, padx=7, pady=5)

dark_button = Button(root, text="Темная", bg="black", fg="white", command=dark_theme)
dark_button.pack(side=LEFT, padx=7, pady=5)

# запускаем главный цикл приложения
root.mainloop()
