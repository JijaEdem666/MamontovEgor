import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
from scipy.optimize import minimize
from scipy.optimize import differential_evolution

def get_path(xc):
    global path
    path.append(xc[0])

mpl.style.use('seaborn-white')
warnings.filterwarnings('ignore')

dx = 0.001
x = np.arange(-10, 10, dx)

f = lambda x: x**2 * (1 - 0.1 * (x) ** 2) * np.exp(-0.1 * (x) ** 2)

x0 = 2.4
path = [x0]
result = minimize(f, x0=x0, tol=1e-2, callback=get_path)
x1 = result.x
print(result)
print()
result1 = minimize(f, x0=1.5)
x2 = result1.x
print(result1)

plt.scatter([x0], [f(x0)], color='tab:green')
plt.plot(path, [f(i) for i in path], '--o', color="black", lw=0.75, markersize=2)
plt.scatter([x1], [f(x1)], color='tab:red')
plt.plot(x, f(x), zorder=0)
plt.xlim(0, 10)
plt.ylim(-3.5, 2)

fig, ax = plt.subplots()
ax.set(xlabel='x', ylabel='f(x)')
ax.plot(x, f(x))

plt.annotate("", xytext=(2.4, f(2.4)), xy=(x1, f(x1)), arrowprops=dict(arrowstyle="->"))
plt.annotate("", xytext=(1.5, f(1.5)), xy=(x2, f(x2)), arrowprops=dict(arrowstyle="->"))
plt.scatter([x1, x2], [f(x1), f(x2)], color='tab:red')
plt.scatter([2.4, 1.5], [f(2.4), f(1.5)], color='tab:green')
plt.plot(x, f(x), zorder=0)

result2 = differential_evolution(f, [(x.min(), x.max())])
print()
print(result2)

plt.show()