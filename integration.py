import numpy as np

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

test_trapezoidal()