import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

f0 = float(input())
dt = 0.001
t = np.arange(0,2,dt)

func = lambda y, t: y + t

res = odeint(func, y0=f0, t=t)

for i in range(len(t)):
    if t[i] == 1:
        print(round(res[i][0], 2))