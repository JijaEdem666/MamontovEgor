from scipy.optimize import minimize
import numpy as np
def func(z, a, b):
    x, y = z[0], z[1]
    return (x + y) ** 2 - 2 * x * (y + a) - 2 * y * b + a + b


a, b = map(float, input().split())
res = minimize(func, ((0, 0) ), args=(a, b))
print(" ".join(str(i) for i in res.x))
