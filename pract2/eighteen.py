import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import differential_evolution

def get_path(xc, convergence=0):
    global path
    path.append(xc)


def gauss(z, sigma, x0, y0):
    x, y = z
    return np.exp(-((x - x0) ** 2 + (y - y0) ** 2) / sigma ** 2)

def mixed(z, *args):
    return np.sum(neg_gauss(z, *params) for params in args)

neg_gauss = lambda z, sigma, x0, y0: -gauss(z, sigma, x0, y0)

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)


a, b = 0, 0

def func(t, a, b):
    x, y = t[0], t[1]
    return (x + y) ** 2 - 2 * x * (y + a) - 2 * y * b + a + b

x0 = (-10, -2)
path = [x0]
result = minimize(mixed, x0, args=((10, -5, -12), (7, 5, 5), (9, -5, 10)), callback=get_path,)
Z = mixed((X, Y), (10, -5, -12), (7, 5, 5), (9, -5, 10))
path = np.array(path)


fig, ax = plt.subplots(1, 2, figsize=(8, 8))
contours = ax[0].contour(X, Y, Z, 16, colors="black", linewidth=2, linestyles='-.')
ax[0].clabel(contours, inline=True, fontsize=16)
contours = ax[0].contourf(X, Y, Z, 200, cmap=plt.cm.jet)
ax[0].scatter(path[:, 0], path[:, 1], s=1600, c='yellow', marker="*", alpha=1, edgecolor='black', linewidth=2, zorder=1)
ax[0].set_title('Gradient')

path = [x0]

result1 = differential_evolution(mixed, ((-20, 20), (-20, 20)), init=np.array([x0, (-9, -1), (-11, -3), (-8, 0), (-12, -4)]),
                                 args=((10, -5, -12), (7, 5, 5), (9, -5, 10)), recombination=0.15, seed=2, callback=get_path)
path = np.array(path)
contours = ax[1].contour(X, Y, Z, 16, colors="black", linewidth=2, linestyles='-.')
ax[1].clabel(contours, inline=True, fontsize=16)
contours = ax[1].contourf(X, Y, Z, 200, cmap=plt.cm.jet)
ax[1].scatter(path[:, 0], path[:, 1], s=1600, c='yellow', marker="*", alpha=1, edgecolor='black', linewidth=2, zorder=1)
ax[1].set_title('DE')

plt.show()