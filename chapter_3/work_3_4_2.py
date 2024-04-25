import numpy as np
from work_3_4_1 import sovle_secant


def fun_x(x):
    return np.cos(x) - x


if __name__ == "__main__":
    root = sovle_secant(fun_x, 0.5, np.pi / 4, 1e-6, 100)
    print(root)
