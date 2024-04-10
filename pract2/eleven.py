import math

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def tox(u, v):
    return (8 * np.exp(-1 * u / 5) + 4 * np.exp(-1 * u / 5) * np.cos(v)) * np.cos(u)

def toy(u, v):
    return (8 * np.exp(-1 * u / 5) + 4 * np.exp(-1 * u / 5) * np.sin(v)) * np.sin(u)

def f(u, v):
    return 4 * np.exp(u) * np.sin(v)



i = np.linspace(0, 30)
j = np.linspace(0, 30)

u = 3 * np.pi * i / 30
v = 2 * np.pi * j / 30

U, V = np.meshgrid(u, v)

X = tox(U, V)
Y = toy(U, V)

Z = f(U, V)
fig, ax = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z, cmap=plt.cm.ocean_r)
ax.view_init(30, 60)
plt.show()