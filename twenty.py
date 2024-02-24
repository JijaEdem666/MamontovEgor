result = 0
x = float(input())
elem = x
i = 1
while abs(elem) >= 10 ** -6:
    result += elem
    i += 1
    elem = (((-1) ** (i - 1)) * x ** i) / i
print(round(result, 8))