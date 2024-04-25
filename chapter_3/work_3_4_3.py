# 对比 弦截法 不动点法 和 牛顿法 的收敛速度
import numpy as np
from work_3_0_1 import timer
from work_3_2_1 import sovle_fixed_point
from work_3_3_1 import sovle_newton
from work_3_4_1 import sovle_secant


def fun_x(x):
    return np.cos(x) - x


def g(x):
    return np.cos(x)


if __name__ == "__main__":
    # 弦截法
    x0 = 0.5
    x1 = np.pi / 4
    sovle_secant = timer(sovle_secant)
    result1, iteration1 = sovle_secant(fun_x, x0, x1, 1e-6, 100)
    print("弦截法结果:", result1, "迭代次数:", iteration1)
    # 不动点法
    x0 = 0.5
    sovle_fixed_point = timer(sovle_fixed_point)
    result2, iteration2 = sovle_fixed_point(g, x0, 1e-6, 100, 10)
    print("不动点法结果:", result2, "迭代次数:", iteration2)
    # 牛顿法
    x0 = 0.5
    sovle_newton = timer(sovle_newton)
    result3, iteration3 = sovle_newton(fun_x, x0, 1e-6, 100)
    print("牛顿法结果:", result3, "迭代次数:", iteration3)
