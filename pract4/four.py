from tkinter import *


def create_label():
    s = entry.get()
    label = Label(text=f"Привет {s}")
    label.pack()


root = Tk()
root.geometry("300x150")
root.title("Задание 4")
root.config(bg="orange")

entry = Entry(width=50, background="DeepSkyBlue", foreground="white", borderwidth=5, relief="solid", font=("Arial", 12))
entry.insert(0 ,"Введите ваше имя:")
entry.pack()

bt = Button(text="Нажмите",command=create_label, bg="white", fg="DodgerBlue", borderwidth=1, relief="solid", font=("Arial", 11))
bt.pack()

root.mainloop()
