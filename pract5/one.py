from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Визуализация триангуляционных данных")

choosebutton = Button(text="Выбрать файл")
choosebutton.place(x=0, y=0, width=500, height=100)

visualbutton = Button(text="Визуализация")
visualbutton.place(x=0, y=100, width=500, height=100)

root.mainloop()
