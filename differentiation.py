from logging import exception
import numpy as np

def input_data():
    data_x = np.array([])
    data_y = np.array([])

    n = int(input("Enter the number of points: "))

    for i in range(n):
        data_x = np.append(data_x, float(input("X[{}]: ".format(i))))

    for i in range(n):
        data_y = np.append(data_y, float(input("Y[{}]: ".format(i))))

    x = float(input("Find dY/dX for X = "))

    return [data_x, data_y, x]

def forward_difference_first_order(data_x, data_y, x):
    if x == data_x[-1]:
        raise Exception("The derivative of the last point can't be obtained using forward difference")

    idx = np.where(data_x == x)
    if idx[0].size == 0:
        raise Exception("The X point isn't in the given data")
    else:
        return (data_y[idx[0][0] + 1] - data_y[idx[0][0]])/(data_x[idx[0][0] + 1] - data_x[idx[0][0]])

def forward_difference_second_order(data_x, data_y, x):
    if x == data_x[-1] or x == data_x[-2]:
        raise Exception("The derivative of the last two points can't be obtained using forward difference")

    dx = data_x[1] - data_x[0]
    for i in range(2, data_x.size):
        # Allowed error is 1e-4
        if abs(data_x[i] - data_x[i - 1] - dx) > 1e-4:
            raise Exception("All the points should be equally spaced")

    idx = np.where(data_x == x)
    if idx[0].size == 0:
        raise Exception("The X point isn't in the given data")
    else:
        return (data_y[idx[0][0] + 2] - 2 * data_y[idx[0][0] + 1] + data_y[idx[0][0]])/(dx * dx)

def backward_difference_first_order(data_x, data_y, x):
    if x == data_x[0]:
        raise Exception("The derivative of the first point can't be obtained using backward difference")

    idx = np.where(data_x == x)
    if idx[0].size == 0:
        raise Exception("The X point isn't in the given data")
    else:
        return (data_y[idx[0][0]] - data_y[idx[0][0] - 1])/(data_x[idx[0][0]] - data_x[idx[0][0] - 1])

def centered_difference_first_order(data_x, data_y, x):
    if x == data_x[0] or x == data_x[-1]:
        raise Exception("The derivative of the first and last point can't be obtained using centered difference")

    idx = np.where(data_x == x)
    if idx[0].size == 0:
        raise Exception("The X point isn't in the given data")
    else:
        return (data_y[idx[0][0] + 1] - data_y[idx[0][0] - 1])/(2 * (data_x[idx[0][0]] - data_x[idx[0][0] - 1]))

def centered_difference_second_order(data_x, data_y, x):
    if x == data_x[-1] or x == data_x[0]:
        raise Exception("The derivative of the last two points can't be obtained using forward difference")

    dx = data_x[1] - data_x[0]
    for i in range(2, data_x.size):
        # Allowed error is 1e-4
        if abs(data_x[i] - data_x[i - 1] - dx) > 1e-4:
            raise Exception("All the points should be equally spaced")

    idx = np.where(data_x == x)
    if idx[0].size == 0:
        raise Exception("The X point isn't in the given data")
    else:
        return (data_y[idx[0][0] + 1] + data_y[idx[0][0] - 1] - 2*data_y[idx[0][0]])/(dx * dx)

def test_forward_difference():
    data_x, data_y, x = input_data()
    dy = forward_difference_first_order(data_x, data_y, x)
    print("dY/dX at X = {} : {}".format(x, dy))
    dy2 = forward_difference_second_order(data_x, data_y, x)
    print("d2Y/dX2 at X = {} : {}".format(x, dy2))

def test_backward_difference():
    """
    Example:
        X = 1, 2, 4
        Y = 1.1, 0.7, 0.4
        dY/dX at X = 2 : -0.4
    """
    data_x, data_y, x = input_data()
    dy = backward_difference_first_order(data_x, data_y, x)
    print("dY/dX at X = {} : {}".format(x, dy))

def test_centered_difference():
    """
    Example:
        X = 1.0, 1.2, 1.4, 1.6
        Y = 1.359, 1.660, 2.028, 2.477
        dY/dX at X = 1.4 : 2.043
        d2Y/dX2 at X = 1.4 : 2.025
    """
    data_x, data_y, x = input_data()
    dy = centered_difference_first_order(data_x, data_y, x)
    print("dY/dX at X = {} : {}".format(x, dy))
    dy2 = centered_difference_second_order(data_x, data_y, x)
    print("d2Y/dX2 at X = {} : {}".format(x, dy2))