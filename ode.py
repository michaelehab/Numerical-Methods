import numpy as np
import math

def f1(t, y):
    return (y / t)**2 + (y / t)

def df1(t, y):
    return (2 * y**3 / t**4) + (y**2 / t**3)

def f2(t, y):
    return math.sin(t) + math.exp(-t)

def df2(t, y):
    return math.cos(t) - math.exp(-t)

def f3(t, y):
    return (2 / t) * y + t**2 * math.exp(t)

def f4(t, y):
    return (1 / t**2) - (y / t)

def euler(f, y0, t0, h, start_t, end_t):
    ans = []
    ans.append(y0 + f(t0, y0) * h)
    while t0 + h < end_t:
        t0 += h
        ans.append(ans[-1] + f(t0, ans[-1]) * h)
    return ans

def taylor(f, df, y0, t0, h, start_t, end_t):
    ans = []
    ans.append(y0 + f(t0, y0) * h)
    while t0 + h < end_t:
        t0 += h
        ans.append(ans[-1] + f(t0, ans[-1]) * h + 0.5 * df(t0, ans[-1]) * h**2)
    return ans

def rk2(f, y0, t0, h, start_t, end_t, a1, a2, p1, q1):
    ans = []
    k1 = f(t0, y0)
    k2 = f(t0 + p1 * h, y0 + q1 * h * k1)
    ans.append(y0 + h * (a1 * k1 + a2 * k2))
    while t0 + h < end_t:
        t0 += h
        k1 = f(t0, ans[-1])
        k2 = f(t0 + p1 * h, ans[-1] + q1 * h * k1)
        ans.append(ans[-1] + h * (a1 * k1 + a2 * k2))
    return ans

def rk4(f, y0, t0, h, start_t, end_t):
    ans = []
    k1 = f(t0, y0)
    k2 = f(t0 + 0.5 * h, y0 + 0.5 * h * k1)
    k3 = f(t0 + 0.5 * h, y0 + 0.5 * h * k2)
    k4 = f(t0 + h, y0 + h * k3)
    ans.append(y0 + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4))
    while t0 + h < end_t:
        t0 += h
        k1 = f(t0, ans[-1])
        k2 = f(t0 + 0.5 * h, ans[-1] + 0.5 * h * k1)
        k3 = f(t0 + 0.5 * h, ans[-1] + 0.5 * h * k2)
        k4 = f(t0 + h, ans[-1] + h * k3)
        ans.append(ans[-1] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4))
    return ans

def test_euler():
    """ ans = euler(f1, 1, 1, 0.1, 1, 1.2)
    for i in ans:
        print(i) """
    ans = euler(f2, 0, 0, 0.5, 0, 1)
    for i in ans:
        print(i)

def test_taylor():
    """ ans = taylor(f1, df1, 1, 1, 0.1, 1, 1.2)
    for i in ans:
        print(i) """
    ans = taylor(f2, df2, 0, 0, 0.5, 0, 1)
    for i in ans:
        print(i)

def test_heun():
    ans = rk2(f3, 0, 1, 0.1, 1, 1.2, 0.5, 0.5, 1, 1)
    for i in ans:
        print(i)

def test_midpoint():
    ans = rk2(f4, -1, 1, 0.1, 1, 1.2, 0, 1, 0.5, 0.5)
    for i in ans:
        print(i)

def test_rk4():
    ans = rk4(f4, -1, 1, 0.2, 1, 1.2)
    for i in ans:
        print(i)

test_rk4()