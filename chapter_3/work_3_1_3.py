import numpy as np
from work_3_0_1 import paprmeter_supplementation  # 参数补充装饰器
from work_3_1_1 import solve_BisMethod

CONSTANT_G = 9.8


def fun_x(t, omega, flu_c=0):
    return -CONSTANT_G / (2 * omega**2) * (
        (np.exp(omega * t) - np.exp(-omega * t)) / 2 -
        np.sin(omega * t)) - flu_c


if __name__ == "__main__":
    t = 1
    flu_c = 1.7
    to_param = "omega"
    param = {"t": t, "flu_c": flu_c}
    fun_x = paprmeter_supplementation(to_param, param)(fun_x)
    print(solve_BisMethod(fun_x, -2, 2.1, 1e-5, 1000))
