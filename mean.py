import numpy as np

from urllib.request import urlopen

f = urlopen(input())
houses = np.loadtxt(f, skiprows=1, delimiter=",")
print(houses.mean(0))
