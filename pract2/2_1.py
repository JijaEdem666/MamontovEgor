import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
x1 = np.square(np.sin(2 * x))
x2 = np.exp(np.square((x + 2) / 10))
y = np.linspace(-10, 10, 1000)
y = np.square(np.sin(2 * x)) * np.exp(np.square((x + 2) / 10))
plt.figure(figsize=(8, 3))
plt.grid(lw=0.5, ls='--')
plt.plot(x, y, lw=4.0, color='red')
plt.plot(x, y, lw=4.0, color='black', zorder=0)
plt.show()