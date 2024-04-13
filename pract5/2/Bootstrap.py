import config
from MainApp import MainApp


class Bootstrap():

    @staticmethod
    def initEnviroment():
        config.mainApp = MainApp()
        config.mainApp.title("Визуализация триангуляционных данных")
        config.mainApp.iconbitmap("aData/exchange.ico")
        config.mainApp.geometry('1000x700')

    @staticmethod
    def run():
        config.mainApp.mainloop()
