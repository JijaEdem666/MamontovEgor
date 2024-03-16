from tkinter import *
from tkinter import messagebox as mb

math = ""
f_num = ''


def button_add():
    global f_num, math
    math = "+"
    try:
        f_num = int(entry.get())
    except:
        mb.showerror("Ошибка!", "Строка должна содержать только цифры!\n Попробуйте заново.")
        f_num = 0
        math = ""
    entry.delete(0, END)


def button_subtract():
    global f_num, math
    math = "-"
    try:
        f_num = int(entry.get())
    except:
        mb.showerror("Ошибка!", "Строка должна содержать только цифры!\n Попробуйте заново.")
        f_num = 0
        math = ""
    entry.delete(0, END)


def button_multiply():
    global f_num, math
    math = "*"
    try:
        f_num = int(entry.get())
    except:
        mb.showerror("Ошибка!", "Строка должна содержать только цифры!\n Попробуйте заново.")
        f_num = 0
        math = ""
    entry.delete(0, END)


def button_divide():
    global f_num, math
    math = "/"
    try:
        f_num = int(entry.get())
    except:
        mb.showerror("Ошибка!", "Строка должна содержать только цифры!\n Попробуйте заново.")
        f_num = 0
        math = ""
    entry.delete(0, END)


def button_click(n):
    entry.insert(END, f"{n}")


def clear():
    entry.delete(0, END)


def button_equal():
    global f_num, math
    try:
        s_num = int(entry.get())
    except:
        mb.showerror("Ошибка!", "Строка должна содержать только цифры!\n Попробуйте заново.")
        return
    entry.delete(0, END)
    match math:
        case "+":
            entry.insert(0, str(f_num + s_num))
        case "-":
            entry.insert(0, str(f_num - s_num))
        case "*":
            entry.insert(0, str(f_num * s_num))
        case "/":
            try:
                entry.insert(0, str(f_num // s_num))
            except:
                mb.showerror("Ошибка!", "Не может быть деления на 0!")
                return
        case _:
            mb.showerror("Ошибка!", "Вы не выбрали операцию!")
    math = ""


root = Tk()
root.geometry("600x700")
root.title("Калькулятор")

entry = Entry(font=("Arial", 13))
entry.place(x=100, y=25, width=400, height=50)

for i in range(3, 10, 3):
    btn_clk = lambda x=i-2: button_click(x)
    button1 = Button(text=f"{i - 2}", command=btn_clk)
    button1.place(x=0, y=(3 - (i / 3)) * 100 + 100, width=200, height=100)

    btn_clk = lambda x=i - 1: button_click(x)
    button2 = Button(text=f"{i - 1}", command=btn_clk)
    button2.place(x=200, y=(3 - (i / 3)) * 100 + 100, width=200, height=100)

    btn_clk = lambda x=i: button_click(x)
    button3 = Button(text=f"{i}", command=btn_clk)
    button3.place(x=400, y=(3 - (i / 3)) * 100 + 100, width=200, height=100)

btn_clk = lambda x=0: button_click(x)
button0 = Button(text="0", command=btn_clk)
button0.place(x=0, y=400, width=200, height=100)

button_clear = Button(text="Очистить", command=clear)
button_clear.place(x=200, y=400, width=400, height=100)

button_add = Button(text="+", command=button_add)
button_add.place(x=0, y=500, width=200, height=100)

button_subtract = Button(text="-", command=button_subtract)
button_subtract.place(x=0, y=600, width=200, height=100)

button_multiply = Button(text="*", command=button_multiply)
button_multiply.place(x=200, y=600, width=200, height=100)

button_divide = Button(text="/", command=button_divide)
button_divide.place(x=400, y=600, width=200, height=100)

button_equal = Button(text="=", command=button_equal)
button_equal.place(x=200, y=500, width=400, height=100)

root.mainloop()
