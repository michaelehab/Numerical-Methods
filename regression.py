import numpy as np

def linear_regression(data_x, data_y):
    n1 = data_x.size
    n2 = np.sum(data_x)
    n3 = np.sum(np.square(data_x))
    n4 = np.sum(data_y)
    n5 = 0
    for i in range(data_x.size):
        n5 += (data_x[i] * data_y[i])

    b = (n4 + (-n1 / n2) * n5) / (n2 + (-n1 / n2) * n3)
    a = (n4 - n2 * b) / n1

    return [a, b]

def test_linear_regression():
    """
    Example:
        Data_x = 2, 4, 6, 8
        Data_y = 2, 11, 28, 40
        b = -12.5
        a = 6.55

    Note:
        In case of non linear models like y = a * e ^ (bx)
        We have to linearize it to obtain a function to use with linear regression
        So, by taking ln() of the two sides we get: ln(y) = ln(a) + bx
        We can then use linear regression with each y = ln(y) and x = ln(x)
    """
    print("Testing Linear Regression:")

    data_x = np.array([])
    data_y = np.array([])

    n = int(input("Enter the number of points: "))

    for i in range(n):
        data_x = np.append(data_x, float(input("X[{}]: ".format(i))))

    for i in range(n):
        data_y = np.append(data_y, float(input("Y[{}]: ".format(i))))

    a, b = linear_regression(data_x, data_y)
    print("Y = {}X + {}".format(b, a))

test_linear_regression()
