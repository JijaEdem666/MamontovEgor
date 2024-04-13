from tkinter import *
from tkinter import messagebox as mb
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from CommonUtils import CommonUtils
import config

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.button_choose = Button(text="Выбрать файл", command=CommonUtils.load_txt)
        self.button_choose.place(x=0, y=0, width=300, height=100)
        self.button_show = Button(text="Отобразить", command=self.err)
        self.button_show.place(x=0, y=100, width=300, height=100)

        self.state = StringVar(value="0")
        self.radio1 = Radiobutton(text="Линия", variable=self.state, value="0")
        self.radio1.place(x=750, y=50)
        self.radio2 = Radiobutton(text="Свеча", variable=self.state, value="1")
        self.radio2.place(x=750, y=150)

    def err(self):
        mb.showerror("Ошибка", config.errorDataImport)

    def show(self):
        if self.state.get() == "0":
            self.fig, self.ax = plt.subplots(figsize=(10,4))

            y = np.array(config.res_dict["high"])
            x = np.array(config.res_dict["date"])


            self.ax.plot(x, y)
            self.ax.set_xticks(["2020-01-03", "2020-07-02", "2021-01-04", "2021-07-01", "2022-01-03", "2022-07-01", "2023-01-03", "2023-07-03", "2024-01-01"])
            self.ax.set_xticklabels(["2020-01", "2020-07", "2021-01", "2021-07", "2022-01", "2022-07", "2023-01", "2023-07", "2024-01"])

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=500, y=200, anchor=N)

            toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
            toolbar.update()
            toolbar.place(x=500, y=700, anchor=N)
        else:
            self.fig, self.ax = plt.subplots(figsize=(10, 4))



            for i in range(10, len(config.res_dict["date"]), 10):
                if config.res_dict["close"][i-10] > config.res_dict["close"][i]:
                    self.ax.bar(config.res_dict["date"][i], height=config.res_dict["close"][i-10] - config.res_dict["close"][i], bottom=config.res_dict["close"][i], width=0.4, align='center', color='red')
                    self.ax.bar(config.res_dict["date"][i], height=max(config.res_dict["high"][i-10:i+1]) - min(config.res_dict["low"][i-10:i+1]), bottom=min(config.res_dict["low"][i-10:i+1]), width=0.05, align='center', color='red')
                else:
                    self.ax.bar(config.res_dict["date"][i], height=config.res_dict["close"][i] - config.res_dict["close"][i-10], bottom=config.res_dict["close"][i-10], width=0.4,
                                align='center', color='green')
                    self.ax.bar(config.res_dict["date"][i], height=max(config.res_dict["high"][i-10:i+1]) - min(config.res_dict["low"][i-10:i+1]), bottom=min(config.res_dict["low"][i-10:i+1]), width=0.05,
                                align='center', color='green')


            self.ax.set_xticks(
                ["2020-01-03", "2020-07-02", "2021-01-04", "2021-07-01", "2022-01-03", "2022-07-01", "2023-01-03",
                 "2023-07-03", "2024-01-01"])
            self.ax.set_xticklabels(
                ["2020-01", "2020-07", "2021-01", "2021-07", "2022-01", "2022-07", "2023-01", "2023-07", "2024-01"])

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=500, y=200, anchor=N)

            toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
            toolbar.update()
            toolbar.place(x=500, y=700, anchor=N)