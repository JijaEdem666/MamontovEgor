from tkinter import *

root = Tk()
root.config(background="orange")
root.geometry("400x100")

button = Button(text="Hello World!", background="DodgerBlue", foreground="white", borderwidth="0")
button.config(width=12, height=3)
button.pack()


root.mainloop()
