import numpy as np
from urllib.request import urlopen

f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
data = np.loadtxt(f, delimiter=',', skiprows=1)
y = np.array([data[:, 0]]).T
data[:, 0] = 1
X = data
B = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
answer = " ".join(map(str, B.flatten()))
print(answer)
