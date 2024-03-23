import pathlib
from tkinter import *
from PIL import ImageTk, Image
from pathlib import *


def forward(n):
    global i
    i += 1
    label.config(image=images[1])
    label_info.config(text=f"Image {i} of {len(images)}")
    button_forward.config(state=DISABLED)
    button_backward.config(state=NORMAL)


def backward(n):
    global i
    i -= 1
    label.config(image=images[0])
    label_info.config(text=f"Image {i} of {len(images)}")
    button_backward.config(state=DISABLED)
    button_forward.config(state=NORMAL)


def exit_program():
    root.quit()


root = Tk()
root.geometry("700x700")
root.title("Photo Viewer")
file = pathlib.Path().joinpath("test_axe.ico").resolve()
root.iconbitmap(file)

images = [ImageTk.PhotoImage(Image.open("images/test.png").reduce(5)), ImageTk.PhotoImage(Image.open("images/test2.png").reduce(5))]

label = Label(image=images[0])
label.place(x=350 - images[0].width() / 2, y=250 - images[0].height() / 2)

fwrd = lambda x=1: forward(x)
button_forward = Button(text=">>", command=fwrd)
button_forward.place(x=700-100, y=700-100)

bwrd = lambda x=1: backward(x)
button_backward = Button(text="<<", state=DISABLED, command=bwrd)
button_backward.place(x=100, y=700-100)

i = 1

label_info = Label(text=f"Image {i} of {len(images)}", bd=1, relief=SUNKEN, anchor=E)
label_info.place(x=700-100, y=700-50)

button_exit = Button(text="Exit Program", command=exit_program)
button_exit.place(x=350-35, y=700-100)

root.mainloop()
