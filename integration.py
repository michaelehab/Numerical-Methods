import numpy as np
import math

def f1(x):
    return 1 / (1 + x)

def trapezoidal(start, end, n):
    h = float((end - start) / n)
    print("H = {}".format(h))
    ans = f1(start) + f1(end)
    while(start + h != end):
        ans += 2 * f1(start + h)
        start += h
    return ans * (h / 2)

def simpson(start, end, n):
    h = float((end - start) / n)
    ans = f1(start) + f1(end)
    i = 0
    while(start + h != end):
        if i % 2 == 0 : 
            ans += 4 * f1(start + h)
        else:
            ans += 2 * f1(start + h)
        start += h
        i += 1
    return ans * (h / 3)  

def midpoint(start, end):
    return (end - start) * f1((start + end) / 2)

def two_points_gauss_quadrature(start, end):
    x = (end - start) / 2
    y = (end + start) / 2
    return x * (f1(x * (-1 / math.sqrt(3)) + y) + f1(x * (1 / math.sqrt(3)) + y))

def test_trapezoidal():
    """
    Example:
        F(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09545
    """
    print("Integrating F(x) using Trapezoidal rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    n = int(input("Enter the number of segments: "))
    ans = trapezoidal(start, end, n)
    print("The answer is {}".format(ans))

def test_simpson():
    """
    Example:
        F(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09531
    """
    print("Integrating F(x) using Simpson rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    n = int(input("Enter the number of segments: "))
    ans = simpson(start, end, n)
    print("The answer is {}".format(ans))

def test_midpoint():
    """
    Example:
        F(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09524
    """
    print("Integrating F(x) using Midpoint rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    ans = midpoint(start, end)
    print("The answer is {}".format(ans))

def test_gauss_quadrature():
    """
    Example:
        F(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09531
    """
    print("Integrating F(x) using Two Points Gauss Quadrature rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    ans = two_points_gauss_quadrature(start, end)
    print("The answer is {}".format(ans))

test_gauss_quadrature()