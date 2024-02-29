import math
import matplotlib.pyplot as plt

def func(x, a0, a1, a2, N):
    """
    Calculate function values for passed array of arguments
    """
    return a0 - a1 * abs(x/N - 1/2)**(-a2) * math.cos(2 * math.pi * x / N)

def tabulate(a, b, n):
    x_values = [a + (b - a) * i / (n - 1) for i in range(n)]
    return x_values

def main():
    a0 = 0.62
    a1 = 0.48
    a2 = 0.38
    N = 7
    
    x_values = tabulate(0, 1, 1000)
    y_values = [func(x, a0, a1, a2, N) for x in x_values]

    plt.plot(x_values, y_values)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
