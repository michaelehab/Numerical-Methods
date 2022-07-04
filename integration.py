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
        F(X) = e^(x) * sin(x)
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
        F(X) = e^(x) * sin(x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09524
    """
    print("Integrating F(x) using Midpoint rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    n = int(input("Enter the number of segments: "))
    ans = midpoint(start, end)
    print("The answer is {}".format(ans))

test_midpoint()