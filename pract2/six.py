import numpy as np
def nonzero(A):
    for i in range(100):
        for j in range(100):
            if A[i, j] != 0:
                return i, j
    return "нет ненулевого"


A = np.zeros((100, 100))
A[56, 70] = 1
print(nonzero(A))