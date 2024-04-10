from tkinter import *
import appSettings

class MainWindow(Tk):
    def __init__(self):
        self.geometry("1000x700")
        self.title("Анализ видео")
        button_pause = Button(self, text="Пауза", font=("Arial", 10))
        button_pause.place(x=50, y=600)
        button_photo = Button(self, text="Снимок")
        button_photo.place(x=200, y=600)
