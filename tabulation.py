import math
import numpy as np
from matplotlib import pyplot as plt

def func(x: np.ndarray, a0: float, a1: float, a2: float, N: int) -> np.ndarray:
    """
    Calculate function values for passed array of arguments
    """
    return a0 - a1 * np.abs(x/N - 1/2)**(-a2) * np.cos(2 * np.pi * x / N)

def tabulate(a: float, b: float, n: int) -> tuple[np.ndarray, np.ndarray]:
    x = np.linspace(a, b, n)
    return x

def main():
    a0 = 0.62
    a1 = 0.48
    a2 = 0.38
    N = 7
    
    x_values = tabulate(0, 1, 1000)
    y_values = func(x_values, a0, a1, a2, N)

    plt.plot(x_values, y_values)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
