import numpy as np
I = np.eye(2)
print(I)
A = np.array([[0, 1], [1, 0]])
print(A)
x = np.sum(np.dot(A, I))
y = np.sum(A * I)
print(x, y)