import tkinter
from tkinter import *


class MainWindow(Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)
        self.principal = DoubleVar()
        self.rate = DoubleVar()
        self.years = IntVar()
        self.amount = StringVar()
        principalLabel = Label(text="Principal $:", underline=0, anchor=tkinter.W)
        principalScale = Scale(variable=self.principal, command=self.updateUi, from_=100, to=10**6, resolution=100, orient=tkinter.HORIZONTAL, length=300)
        rateLabel = Label(text="Rate %:", underline=0, anchor=tkinter.W)
        rateScale = Scale(variable=self.rate, command=self.updateUi, from_=0, to=100, resolution=0.01, orient=tkinter.HORIZONTAL, length=300)
        yearsLabel = Label(text="Years:", underline=0, anchor=tkinter.W)
        yearsScale = Scale(variable=self.years, command=self.updateUi, from_=1, to=100, resolution=1, orient=tkinter.HORIZONTAL, length=300)
        amountLabel = Label(text="Amount $", underline=0, anchor=tkinter.W)
        actualAmountLabel = Label(textvariable=self.amount, relief=tkinter.SUNKEN, anchor=tkinter.E)
        principalLabel.grid(column=0, row=0)
        principalScale.grid(column=1, row=0)
        rateLabel.grid(column=0, row=1)
        rateScale.grid(column=1, row=1)
        yearsLabel.grid(column=0, row=2)
        yearsScale.grid(column=1, row=2)
        amountLabel.grid(column=0, row=3)
        actualAmountLabel.grid(column=1, row=3)
        self.parent.bind("<Escape>", self.quit)
        self.updateUi()
        self.parent.mainloop()
    def updateUi(self, *ignore):
        self.amount.set(str(round(self.principal.get() * (1 + self.rate.get() / 100) ** self.years.get(), 2)))

    def quit(self, event=None):
        self.parent.destroy()

