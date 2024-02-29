import numpy as np
from matplotlib import pyplot as plt

def func_py(x, a0, a1, a2, N):
   
    return a0 - a1 * np.abs(x/N - 1/2)**(-a2) * np.cos(2 * np.pi * x / N)

def tabulate_py(a, b, n):
    x = np.linspace(a, b, n)
    y = func_py(x, a0=0.62, a1=0.48, a2=0.38, N=7)
    return x, y

def tabulate_np(a, b, n):
    x = np.linspace(a, b, n)
    y = func_py(x, a0=0.62, a1=0.48, a2=0.38, N=7)  
    return x, y

def test_tabulation(f, a, b, n, axis):
    res = f(a, b, n)
    axis.plot(res[0], res[1])
    axis.grid()

def main():
    a, b, n = 0, 1, 1000

    fig, (ax1, ax2) = plt.subplots(2, 1)
    test_tabulation(tabulate_py, a, b, n, ax1)
    test_tabulation(tabulate_np, a, b, n, ax2)
    plt.show()

if __name__ == '__main__':
    main()
