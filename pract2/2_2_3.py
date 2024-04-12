import numpy as np
import matplotlib.pyplot as plt

y1 = np.random.normal(-10, 7, 10**7)
y2 = np.random.normal(10, 5, 10**7)
y3 = np.random.normal(25, 10, int(1.5 * 10**7))

y = np.concatenate([y1, y2, y3])

plt.hist(y, range=(-40, 80), bins=100, density=True)
plt.show()