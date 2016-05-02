import numpy as np


def sigmoid(x):
    """сигмоидальная функция, работает и с числами, и с векторами (поэлементно)"""
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    """производная сигмоидальной функции, работает и с числами, и с векторами (поэлементно)"""
    return sigmoid(x) * (1 - sigmoid(x))

def calculate_dJ_dw(x, w_2, w_3, y, special=False):
    z_2 = w_2.T.dot(x)
    a_2 = sigmoid(z_2)
    if special:
        a_2[0][0] = max(z_2[0][0], 0.0)

    z_3 = w_3.T.dot(a_2)
    a_3 = sigmoid(z_3)
    delta_3 = (a_3 - y) * sigmoid_prime(z_3)
    print(delta_3)
    if special:
        prime = np.array([[int(z_2[0][0] > 0)], [sigmoid_prime(z_2[1][0])]])
        delta_2 = (w_3.dot(delta_3)) * prime
    else:
        delta_2 = (w_3.dot(delta_3)) * sigmoid_prime(z_2)
    dJ_dw = x.dot(delta_2.T)
    return dJ_dw


# 3_3_2
x = np.array([[0.0],
              [1.0],
              [2.0]])
w_2 = np.array([[2.0, 2.0],
                [2.0, 2.0],
                [2.0, 2.0]])
w_3 = np.array([[1.0],
                [1.0]])
y = np.array([[1]])
print(calculate_dJ_dw(x, w_2, w_3, y))

# 3_3_3
x = np.array([[0.0],
              [1.0],
              [2.0]])
w_2 = np.array([[8.0, 10.0],
                [7.0, 10.0],
                [8.0, 9.0]])
w_3 = np.array([[10.0],
                [9.0]])
y = np.array([[1]])
print(calculate_dJ_dw(x, w_2, w_3, y))

# 3_3_4
x = np.array([[15.0],
              [5.0],
              [15.0]])
w_2 = np.array([[0.2, 0.2],
                [0.9, 0.3],
                [0.6, 0.7]])
w_3 = np.array([[0.2],
                [0.5]])
y = np.array([[1]])
print(calculate_dJ_dw(x, w_2, w_3, y))

# 3_3_5
x = np.array([[0.0],
              [1.0],
              [1.0]])
w_2 = np.array([[0.7, 0.8],
                [0.2, 0.3],
                [0.7, 0.6]])
w_3 = np.array([[0.2],
                [0.4]])
y = np.array([[1]])
print(calculate_dJ_dw(x, w_2, w_3, y, True))
