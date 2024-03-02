import numpy as np


def closest(vecs, v, r):
    k = 0
    vec = np.array(vecs[v])
    for i in range(len(vecs)):
        vecs[i] -= vec
    vecs = np.square(vecs)
    vecs = np.sum(vecs, axis=1)
    vecs = np.sqrt(vecs)
    for i in range(len(vecs)):
        if i != v:
            if vecs[i] < r:
                k += 1
    return k


r = float(input())
v = int(input())
vecs = np.array(
    [
        [1.0, 0.0, 2.0],
        [-1.0, 0.5, 2.0],
        [-2.0, 1.5, 0.0],
        [2.5, -1.2, -0.5],
        [1.5, 0.2, -0.2]
    ]
)
print(closest(vecs, v, r))