from tkinter import Tk, Button, Label

from example1.newWindow import NewWindow
from func import Func


def create_new_window():
    gW = NewWindow()
    gW.geometry("250x350+200+100")
    gW.mainloop()

root = Tk()
label = Label(root, text='Текст')
label.pack()
button1 = Button(root, text='Открыть доп.окно', command=lambda: Func(root, label)).pack()
button2 = Button(root, text='Открыть новое окно', command=lambda: create_new_window()).pack()
root.geometry("250x150+300+300")
root.mainloop()