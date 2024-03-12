import numpy as np
from matplotlib import pyplot as plt
import timeit

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

def main():
    a, b, n = 0, 1, 1000

    n_values = np.array((1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000), dtype="uint32")
    t_py = np.full_like(n_values, 0, dtype=float)
    t_np = np.full_like(n_values, 0, dtype=float)
    for i in range(len(n_values)):
        t_py[i] = 1_000_000 * timeit.timeit(f"tabulate_py(0, 1, {n_values[i]})", number=100, globals=globals()) / 100
        t_np[i] = 1_000_000 * timeit.timeit(f"tabulate_np(0, 1, {n_values[i]})", number=100, globals=globals()) / 100

    
    plt.plot(n_values, t_py/t_np) 
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
