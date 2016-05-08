import numpy as np

sizes = [2, 3, 1]
print(sizes[:-1])
print(sizes[1:])

w = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
print(w)
