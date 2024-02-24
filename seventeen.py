pol = input()
mas = "abcdefgh"
col = pol[0]
row = int(pol[1])
if row % 2 == 0:
    if (mas.index(col) + 1) % 2 == 0:
        print("black")
    else:
        print("white")
else:
    if (mas.index(col) + 1) % 2 == 0:
        print("white")
    else:
        print("black")