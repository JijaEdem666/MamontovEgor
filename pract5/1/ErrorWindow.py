import tkinter.messagebox

class ErrorWindow:
    def __init__(self, master, errortext):
        self.error = tkinter.messagebox.showerror("Ошибка!", errortext)