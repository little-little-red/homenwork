import numpy as np
from work_3_3_1 import sovle_newton


def fun_x(x):
    return np.cos(x) - x


if __name__ == "__main__":
    root = sovle_newton(fun_x, 0, 1e-6, 100)
    print(root)
