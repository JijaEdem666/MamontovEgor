from tkinter import Tk, Label, Button


class NewWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.label = Label(self, text="Дополнительное окно").pack()
        self.button = Button(self, text='закрыть', command=lambda: quit()).pack()


    def quit(self, event=None) -> None:
        self.destroy()