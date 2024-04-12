import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 250)

y = 20 * np.sin(x)

for i in range(len(y)):
    print(y[i])
    y[i] += np.random.normal(1, 4)

plt.figure(figsize=(10, 5))
plt.scatter(x, y, s=300, marker='s', c='violet', lw=2, edgecolor='black', hatch='**')
plt.title(label='$sin(x)$ with random noise', fontsize=20)
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)
plt.xticks(ticks=np.arange(-10, 11, 2))
plt.yticks(ticks=np.arange(-20, 21, 6), labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все='][::-1])
plt.show()