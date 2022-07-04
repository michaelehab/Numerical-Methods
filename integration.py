import numpy as np
import math

def f1(x):
    return 1 / (1 + x)

def f2(x):
    return math.tan(x)

def f3(x):
    return x * math.sin(x)

def trapezoidal(start, end, n, f):
    h = float((end - start) / n)
    ans = f(start) + f(end)
    while(start + h != end):
        ans += 2 * f(start + h)
        start += h
    return ans * (h / 2)

def simpson(start, end, n, f):
    h = float((end - start) / n)
    ans = f(start) + f(end)
    i = 0
    while(start + h != end):
        if i % 2 == 0 : 
            ans += 4 * f(start + h)
        else:
            ans += 2 * f(start + h)
        start += h
        i += 1
    return ans * (h / 3)  

def midpoint(start, end, f):
    return (end - start) * f((start + end) / 2)

def two_points_gauss_quadrature(start, end, f):
    x = (end - start) / 2
    y = (end + start) / 2
    return x * (f(x * (-1 / math.sqrt(3)) + y) + f(x * (1 / math.sqrt(3)) + y))

def test_trapezoidal():
    """
    Example:
        F1(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment = 0.09545

        F2(X) = tan(x)
        Integration from 0 to 0.78539816339 (PI / 4) using 4 segments = 0.3498

        F3(X) = x * sin(x)
        Integration from 0 to 6.28318530718 (2 * PI) using 1 segment = 0
        Integration from 0 to 6.28318530718 (2 * PI) using 2 segments = 0
        Integration from 0 to 6.28318530718 (2 * PI) using 4 segments = -4.935
    """
    print("Integrating F(x) using Trapezoidal rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    n = int(input("Enter the number of segments: "))
    ans = trapezoidal(start, end, n, f3)
    print("The answer is {}".format(ans))

def test_simpson():
    """
    Example:
        F1(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09531
    """
    print("Integrating F(x) using Simpson rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    n = int(input("Enter the number of segments: "))
    ans = simpson(start, end, n, f1)
    print("The answer is {}".format(ans))

def test_midpoint():
    """
    Example:
        F1(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09524
    """
    print("Integrating F(x) using Midpoint rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    ans = midpoint(start, end, f1)
    print("The answer is {}".format(ans))

def test_gauss_quadrature():
    """
    Example:
        F1(X) = 1 / (1 + x)
        Integration from 0 to 0.1 = 0.09531

        F3(X) = x * sin(x)
        Integration from 0 to 6.28318530718 (2 * PI) = -11.06
    """
    print("Integrating F(x) using Two Points Gauss Quadrature rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    ans = two_points_gauss_quadrature(start, end, f3)
    print("The answer is {}".format(ans))

test_trapezoidal()