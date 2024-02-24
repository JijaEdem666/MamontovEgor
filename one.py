room = int(input())
entrance = (room // 8) + (room % 8 > 0)
floor = room - (entrance - 1) * 8
print("Подъезд:", entrance)
print("Этаж:", floor)