from mainWindow import MainWindow
from tkinter import *
import pathlib


def increase(mw):
    if mw.years.get() != 100:
        mw.years.set(mw.years.get() + 1)
    mw.updateUi()


def decrease(mw):
    if mw.years.get() != 1:
        mw.years.set(mw.years.get() - 1)
    mw.updateUi()


def openInterest():
    mw = MainWindow(root)

    changeyear = Menu(popmenu, tearoff=0)
    up = lambda x = mw: increase(x)
    changeyear.add_command(label="Увеличить на 1", command=up)
    down = lambda x = mw: decrease(x)
    changeyear.add_command(label="Уменьшить на 1", command=down)
    popmenu.add_cascade(label="Изменить количество лет", menu=changeyear)


def close():
    root.destroy()


def popup(event):
    popmenu.post(event.x_root, event.y_root)

root = Tk()
root.geometry("500x500")
root.title("Interest")
file = pathlib.Path().joinpath("interest.ico").resolve()
root.iconbitmap(file)
root.bind("<Button-3>", popup)

mainmenu = Menu(root)
root.config(menu=mainmenu)

appmenu = Menu(mainmenu, tearoff=0)
appmenu.add_command(label="Открыть Interest", command=openInterest)

mainmenu.add_cascade(label="Приложения", menu=appmenu)

popmenu = Menu(root, tearoff=0)
popmenu.add_command(label="Закрыть", command=close)

root.mainloop()
