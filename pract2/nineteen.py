from scipy.optimize import minimize
import numpy as np
x0 = float(input())
dx = 0.001
x = np.arange(-4, 4, dx)
f = lambda x: -(x ** 2 * (x - 4) ** 2 * np.exp(-(x ** 2)))
res = minimize(f, x0=x0)
print(round(res.x[0], 2))