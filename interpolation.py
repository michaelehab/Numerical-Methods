import numpy as np
import math

def lagrange(x, y, x_find):
    y_ans = 0

    for i in range(0, x.size):
        p = y[i]
        for j in range(0, x.size):
            if i != j:
                p *= ((x_find - x[j]) / (x[i] - x[j]))
        y_ans += p

    return y_ans

def test_lagrange():
    """ 
    Example:
        X = [1.0, 1.3, 1.5]
        Y = [0.841, 0.964, 0.997]
        P(1.4) = 0.9854
    """
    x = np.array([])
    y = np.array([])

    n = int(input("Enter the number of points you have:  "))

    for i in range(n):
        x = np.append(x, float(input("X[{}]: ".format(i))))

    for i in range(n):
        y = np.append(y, float(input("Y[{}]: ".format(i))))

    x_find = float(input("Find Y for X = "))

    print("x", x)
    print("y", y)

    y_ans = lagrange(x, y, x_find)

    print("F({}) = {}".format(x_find, y_ans))