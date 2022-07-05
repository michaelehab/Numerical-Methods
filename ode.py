import numpy as np
import math

def f1(t, y):
    return (y / t) * (y / t) + (y / t)

def f2(t, y):
    return math.sin(t) + math.exp(-t)

def euler(f, y0, t0, h, start_t, end_t):
    ans = []
    ans.append(y0 + f(t0, y0) * h)
    while t0 + h < end_t:
        t0 += h
        ans.append(ans[-1] + f(t0, ans[-1]) * h)
    return ans

def test_euler():
    """ ans = euler(f1, 1, 1, 0.1, 1, 1.2)
    for i in ans:
        print(i) """
    ans = euler(f2, 0, 0, 0.5, 0, 1)
    for i in ans:
        print(i)

test_euler()