import numpy as np

def normalized_power_method(matrix, v, error):
    prev_guess = 0
    while True:
        v = np.matmul(matrix, v)
        eigenvalue = max(abs(v))
        v /= max(v)
        if(abs(eigenvalue - prev_guess) <= error): 
            return [eigenvalue, v]
        else:
            prev_guess = eigenvalue

def input_data():
    n = int(input("Enter n: "))
    matrix = np.array([[float(x) for x in input(f"Enter row {[i]}: ").split()] for i in range(n)])
    v = np.array([float(x) for x in input(f"Enter Initial Guess: ").split()])
    return [matrix, v]

def test_normalized_power_method():
    """
    Example:
        Matrix = [2 1 1]
                 [1 2 1]
                 [1 1 2]

        Initial guess = [1, 1, 1]

        EigenValue = 4
        EigenVector = [1, 1, 1]
    """

    matrix, v = input_data()
    eigenvalue, eigenvector = normalized_power_method(matrix, v, 1e-4)
    print(eigenvalue, eigenvector)

test_normalized_power_method()