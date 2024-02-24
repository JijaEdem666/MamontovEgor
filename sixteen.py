x0, y0 = map(float, input().split())
ring = "no"
rectangle = "no"
if (1 < (x0 - 1) ** 2 + y0 ** 2 < 2):
    ring = "yes"
#Рисунок не совпадает с уравнением прямоугольника. Чтобы рисунок был верным нужно в уравнении для у поменять - на +
if (abs(x0 - 4) < 2 and abs(y0 + 2) < 3):
    rectangle = "yes"
print(ring, rectangle)