from mainWindow import MainWindow
from tkinter import *
import pathlib

root = Tk()
root.geometry("500x500")
root.title("Interest")
file = pathlib.Path().joinpath("interest.ico").resolve()
root.iconbitmap(file)


mw = MainWindow(root)
