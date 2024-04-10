import math

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(x*x + y * y)/(x * x + y * y)

x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig, ax = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z, cmap=plt.cm.ocean_r)
ax.view_init(30, 60)
plt.show()