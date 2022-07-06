def f1(x1, x2):
    return x1**2 - 10*x1 + x2**2 + 8

def f2(x1, x2):
    return x1 * x2**2 + x1 - 10 * x2 + 8

def g1(x1, x2):
    return (x1**2 + x2**2 + 8) / 10
    
def g2(x1, x2):
    return (x1 * x2**2 + x1 + 8) / 10

def fixed_point(g1, g2, initial_guess, tolerance):
    v1 = g1(initial_guess[0], initial_guess[1])
    v2 = g2(initial_guess[0], initial_guess[1])
    prev_v1, prev_v2 = initial_guess[0], initial_guess[1]
    while True:
        if(abs(v1 - prev_v1) < tolerance):
            return [v1, v2]
        prev_v1, prev_v2 = v1, v2
        v1, v2 = g1(prev_v1, prev_v2), g2(prev_v1, prev_v2)
        

def test_fixed_point():
    initial_guess = [0, 0]
    x1, x2 = fixed_point(g1, g2, initial_guess, 1e-3)
    print("X1 = {}, X2 = {}".format(x1, x2))

test_fixed_point()