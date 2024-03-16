from tkinter import *


def myClick():
    label = Label(text="Нажата кнопка!", fg="white", background="orange")
    label.place(x=300/2-50, y=150/2 + 25, width=100, height=50)


root = Tk()
root.geometry("300x150")

root.config(background="orange")

bt = Button(text="Нажмите",command=myClick, bg="white", fg="DodgerBlue", borderwidth=1, relief="solid")
bt.place(x=300/2 - 50, y=150/2 - 25, width=100, height=50)

root.mainloop()
