import math


def trapez(func, a, b, N):
    step = (b - a) / N
    x1 = a
    result = 0
    for _ in range(N):
        x2 = x1 + step
        result += (eval(func + "(x1)") + eval(func + "(x2)")) / 2 * step
        x1 = x2
    return result


func, a, b, N = map(str, input().split())
a, b, N = int(a), int(b), int(N)
print(round(trapez(func, a, b, N), 8))