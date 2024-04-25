import numpy as np


def Lagrange_inter(x, y):

    def f(t):
        n = len(x)
        p = 0
        for i in range(n):
            L = 1
            for j in range(n):
                if j != i:
                    L *= (t - x[j]) / (x[i] - x[j])
            p += y[i] * L
        return p

    return f


x = np.arange(0, np.pi, 8)
