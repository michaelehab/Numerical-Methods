import numpy as np

def lagrange(data_x, data_y, x):
    y_ans = 0

    for i in range(data_x.size):
        p = data_y[i]
        for j in range(data_x.size):
            if i != j:
                p *= ((x - data_x[j]) / (data_x[i] - data_x[j]))
        y_ans += p

    return y_ans

def newton_divided_difference(data_x, data_y, x):
    c = np.copy(data_y)

    for j in range(1, data_x.size):
        for i in range(data_x.size - 1, j - 1, -1):
            c[i] = float(c[i] - c[i - 1]) / float(data_x[i] - data_x[i - j])

    y_ans = 0
    for i in range(data_x.size):
        f = c[i]
        for j in range(i):
            f *= (x - data_x[j])

        y_ans += f
        
    return y_ans

def input_data():
    data_x = np.array([])
    data_y = np.array([])

    n = int(input("Enter the number of points: "))

    for i in range(n):
        data_x = np.append(data_x, float(input("X[{}]: ".format(i))))

    for i in range(n):
        data_y = np.append(data_y, float(input("Y[{}]: ".format(i))))

    x = float(input("Find Y for X = "))

    return [data_x, data_y, x]

def test_lagrange():
    """ 
    Example:
        data_x = [1.0, 1.3, 1.5]
        data_y = [0.841, 0.964, 0.997]
        P(1.4) = 0.9854
    """

    data_x, data_y, x = input_data()

    y_ans = lagrange(data_x, data_y, x)

    print("Using Lagrange Method:")
    print("F({}) = {}".format(x, y_ans))

def test_newton():
    """ 
    Example:
        data_x = [1.0, 1.3, 1.5]
        data_y = [0.841, 0.964, 0.997]
        P(1.4) = 0.9854
    """

    data_x, data_y, x = input_data()

    y_ans = newton_divided_difference(data_x, data_y, x)

    print("Using Newton Divided Difference Method:")
    print("F({}) = {}".format(x, y_ans))