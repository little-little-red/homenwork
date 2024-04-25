import numpy as np
from work_3_0_1 import paprmeter_supplementation  # 参数补充装饰器
from work_3_2_1 import sovle_fixed_point

CONSTANT_G = 9.8


def fun_s(t, s0, m, k):
    return s0 + (m**2 * CONSTANT_G /
                 k**2) * (1 - np.exp(-k / m * t)) - t * m * CONSTANT_G / k


def g_fun_s(t, s0, m, k):
    return (s0 + (m**2 * CONSTANT_G / k**2) *
            (1 - np.exp(-k / m * t))) / (m * CONSTANT_G / k)


if __name__ == "__main__":
    s0 = 300
    m = 0.25
    k = 0.1
    to_param = "t"
    param = {"s0": s0, "m": m, "k": k}
    g_fun_s = paprmeter_supplementation(to_param, param)(g_fun_s)
    root = sovle_fixed_point(g_fun_s, 0, 1e-2, 100, 100)
    print(root)
