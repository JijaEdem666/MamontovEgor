from tkinter import *
import config
from tkinter import filedialog
import csv
from ErrorWindow import ErrorWindow
from GraphWindow import GraphWindow

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.button_choose = Button(text="Выбрать файл", command=self.load_file)
        self.button_choose.place(x=200, y=0, width=400, height=100, anchor=N)
        self.button_visual = Button(text="Визуализация", command=self.visualize)
        self.button_visual.place(x=200, y=100, width=400, height=100, anchor=N)

    def visualize(self):
        graph = GraphWindow()
        graph.geometry("500x700")
        graph.iconbitmap("data/test_axe.ico")
        graph.mainloop()

    def load_file(self):
        # Загрузка csv
        filepath = filedialog.askopenfilename()
        if filepath != "":
            config.data = []
            with open(filepath, encoding='utf-8') as r_file:
                # Создаем объект reader, указываем символ-разделитель ","
                file_reader = csv.reader(r_file, delimiter=",")
                # Счетчик для подсчета количества строк и вывода заголовков столбцов
                count = 0
                # Считывание данных из CSV файла
                for row in file_reader:
                    if count == 0:
                        # Проверка количества и содержания столбцов
                        if len(row) != 3:
                            ErrorWindow(self, config.errorTextImport)
                            break
                    else:
                        l = []
                        for num in row:
                            l.append(int(num))
                        config.data.append(l)
                    count += 1
            print(config.data)
        else:
            ErrorWindow(self, config.errorTextImport)