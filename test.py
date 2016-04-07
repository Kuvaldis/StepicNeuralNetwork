import numpy as np
import random

a = np.array([[1,2,3],[4,5,6]])
print(a)
np.shape(a) # (2,3)

mat = 2 * np.eye(3, 4) + np.eye(3, 4, 1)
print(2 * np.eye(3, 4) + np.eye(3, 4, 1))
print(mat.reshape(12, 1))

print(a.flatten()) # [1, 2, 3, 4, 5, 6]
print(a.T) # transpose
print(a.reshape((3,2))) # flattens, then filled in new form

w = np.array(random.sample(range(1000), 12)) # flat array with 12 random numbers from 1 to 1000
w = w.reshape((2, 2, 3)) # 3 dimential matrix 2x3x3
print(w)
