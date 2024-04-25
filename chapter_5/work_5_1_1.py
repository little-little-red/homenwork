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


x = np.array([2, 5])
y = np.array([4, 1])
f = Lagrange_inter(x, y)

f_vectorized = np.vectorize(f)

x_val = np.array([0, 1, 3])
y_val = f_vectorized(x_val)
print(y_val)
