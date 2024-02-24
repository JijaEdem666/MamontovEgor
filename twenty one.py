mas = list(map(int, input().split()))
maximum = 0
prev = mas[0]
for cur in mas[1:]:
    if abs(cur - prev) * 100 > maximum:
        maximum = abs(cur - prev) * 100
    prev = cur
print(maximum)