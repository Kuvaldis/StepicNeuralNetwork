import numpy as np

x_shape = tuple(map(int, input().split())) # reads first line from input and maps it to int iterator, then converted into tuple. this is the size nxm
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape) # reads second line and creates flatten array from iterator, then reshapes it to matrix

y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)

if x_shape[1] != y_shape[1]:
  print("matrix shapes do not match")
else:
  print(X.dot(Y.T))
