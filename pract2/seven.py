import numpy as np
a = np.array(list(map(int, input().split())))
b = np.argsort(a)
if len(a) < 3:
    print(b)
else:
    print(b[:3])