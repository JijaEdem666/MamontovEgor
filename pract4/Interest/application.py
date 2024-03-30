from mainWindow import MainWindow
from tkinter import *
import pathlib

def openInterest():
    mw = MainWindow(root)


root = Tk()
root.geometry("500x500")
root.title("Interest")
file = pathlib.Path().joinpath("interest.ico").resolve()
root.iconbitmap(file)

mainmenu = Menu(root)
root.config(menu=mainmenu)

appmenu = Menu(mainmenu, tearoff=0)
appmenu.add_command(label="Открыть Interest", command=openInterest)

mainmenu.add_cascade(label="Приложения", menu=appmenu)

root.mainloop()
