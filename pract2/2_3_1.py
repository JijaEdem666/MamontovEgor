import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.axes(projection='polar')

r = 2 * np.random.random(150)
theta = 2 * np.pi * np.random.random(150)

plt.scatter(theta, r, s=400*r**2, c=theta, cmap='hsv', alpha=0.8)
plt.show()