import math

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def f(x, y):
    return 0.25 * np.sin(0.5 * x ** 2 - y) - np.exp(-((x-5) ** 2 + (y-2) ** 2))


x = np.linspace(2, 8, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig, ax = plt.subplots(1, 1, figsize=(6, 5))
obj = ax.imshow(Z, cmap=plt.cm.seismic, vmin=-2, vmax=1)
fig.colorbar(obj)
plt.show()