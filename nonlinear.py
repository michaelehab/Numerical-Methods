import numpy as np

def f1(x1, x2):
    return x1**2 - 10*x1 + x2**2 + 8

def f2(x1, x2):
    return x1 * x2**2 + x1 - 10 * x2 + 8

def g1(x1, x2):
    return (x1**2 + x2**2 + 8) / 10
    
def g2(x1, x2):
    return (x1 * x2**2 + x1 + 8) / 10

def f3(x1, x2):
    return 4 * x1**2 - 20 * x1 + 0.25 * x2**2 + 8

def pf3px1(x1, x2):
    return 8 * x1 - 20

def pf3px2(x1, x2):
    return 0.5 * x2

def f4(x1, x2):
    return 0.5 * x1 * x2**2 + 2 * x1 - 5 * x2 + 8

def pf4px1(x1, x2):
    return 0.5 * x2 **2 + 2

def pf4px2(x1, x2):
    return x1 * x2 - 5

def fixed_point(g1, g2, initial_guess, tolerance):
    v1 = g1(initial_guess[0], initial_guess[1])
    v2 = g2(initial_guess[0], initial_guess[1])
    prev_v1, prev_v2 = initial_guess[0], initial_guess[1]
    while True:
        if(abs(v1 - prev_v1) < tolerance):
            return [v1, v2]
        prev_v1, prev_v2 = v1, v2
        v1, v2 = g1(prev_v1, prev_v2), g2(prev_v1, prev_v2)

def gauss_seidel(g1, g2, initial_guess, tolerance):
    v1 = g1(initial_guess[0], initial_guess[1])
    v2 = g2(initial_guess[0], initial_guess[1])
    prev_v1, prev_v2 = initial_guess[0], initial_guess[1]
    while True:
        if(abs(v1 - prev_v1) < tolerance):
            return [v1, v2]
        prev_v1, prev_v2 = v1, v2
        v1 = g1(prev_v1, prev_v2)
        v2 = g2(v1, prev_v2)

def J(pf1px1, pf2px1, pf1px2, pf2px2, x1, x2):
    return np.array([[pf1px1(x1, x2), pf1px2(x1, x2)], [pf2px1(x1, x2), pf2px2(x1, x2)]])

def newton(pf1px1, pf2px1, pf1px2, pf2px2, f1, f2, x1, x2, steps):
    for i in range(steps):
        y = np.matmul(np.linalg.inv(J(pf1px1, pf2px1, pf1px2, pf2px2, x1, x2)), np.array([-f1(x1, x2), -f2(x1, x2)]))
        x1 += y[0]
        x2 += y[1]
        print("Iteration {} : X1 = {}, X2 = {}".format(i + 1, x1, x2))

    return [x1, x2]
    

def test_fixed_point():
    initial_guess = [0, 0]
    x1, x2 = fixed_point(g1, g2, initial_guess, 1e-3)
    print("X1 = {}, X2 = {}".format(x1, x2))

def test_gauss_seidel():
    initial_guess = [0, 0]
    x1, x2 = gauss_seidel(g1, g2, initial_guess, 1e-3)
    print("X1 = {}, X2 = {}".format(x1, x2))

def test_newton():
    x1, x2 = newton(pf3px1, pf4px1, pf3px2, pf4px2, f3, f4, 0, 0, 2)
    print("F1(X1, X2) = {}".format(f3(x1, x2)))
    print("F2(X1, X2) = {}".format(f4(x1, x2)))

test_newton()