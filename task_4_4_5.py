import numpy as np

def prb(n):
    c = np.math.factorial(50) / (np.math.factorial(n) * np.math.factorial(50 - n))
    return c * (0.55 ** n) * ((1 - 0.55) ** (50 - n))

n = 0.0
for i in range(26, 50):
    n += prb(i)
n += prb(25) / 2
print(n)