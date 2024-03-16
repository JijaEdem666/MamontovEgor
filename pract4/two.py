from tkinter import *


root = Tk()
root.geometry("300x150")
root.config(bg="orange", padx=50, pady=20)

bt1 = Button(text="Hello World!", background="DodgerBlue", borderwidth=0, foreground="white", width=12, height=5)
bt1.grid(row=0, column=0, padx=3, pady=3)

bt2 = Button(text="Меня зовут \n Мамонтов Егор", background="DodgerBlue", borderwidth=0, foreground="white", width=12, height=5)
bt2.grid(row=1, column=1)

l1 = Label(background="DodgerBlue",  borderwidth=1, foreground="white", width=12, height=5)
l1.grid(row=0, column=1)

l2 = Label(background="DodgerBlue", borderwidth=1, foreground="white", width=12, height=5)
l2.grid(row=1, column=0)

root.mainloop()
