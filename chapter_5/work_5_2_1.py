import numpy as np


def newton_inter(x, y):
    n = len(x)
    f = np.zeros((n, n))
    f[0, :] = y
    for i in range(1, n):
        for j in range(n - i):
            f[i, j] = (f[i - 1, j + 1] - f[i - 1, j]) / (x[i + j] - x[j])

    def f_newton(t):
        p = f[0, 0]
        for i in range(1, n):
            L = 1
            for j in range(i):
                L *= (t - x[j])
            p += f[i, 0] * L
        return p

    return f_newton


if __name__ == '__main__':
    x = np.array([1.0, 1.3, 1.6, 1.9, 2.2])
    y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])
    f = newton_inter(x, y)

    f_vectorized = np.vectorize(f)

    x_val = np.array([1.5])
    y_val = f_vectorized(x_val)
    print(y_val)
