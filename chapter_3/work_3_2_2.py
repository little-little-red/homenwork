import math
from work_3_0_1 import paprmeter_supplementation  # 参数补充装饰器
from work_3_2_1 import sovle_fixed_point
from work_3_1_2 import root  # 在3_1_2.py中用二分法计算了根


def g_a(x):
    return x - x**3 - 4 * x**2 + 10


def g_b(x):
    return math.sqrt(10 / x - 4 * x)


def g_c(x):
    return 1 / 2 * math.sqrt(10 - x**3)


def g_d(x):
    return math.sqrt(10 / (4 + x))


def g_e(x):
    return x - (x**3 + 4 * x**2 - 10) / (3 * x**2 + 8 * x)


if __name__ == "__main__":
    to_param = "x"
    g_a = paprmeter_supplementation(to_param)(g_a)
    g_b = paprmeter_supplementation(to_param)(g_b)
    g_c = paprmeter_supplementation(to_param)(g_c)
    g_d = paprmeter_supplementation(to_param)(g_d)
    g_e = paprmeter_supplementation(to_param)(g_e)
    print(sovle_fixed_point(g_a, root, 1e-6, 100, 2))  # 烂函数，不收敛
    print(sovle_fixed_point(g_b, root, 1e-6, 100, 1.5))  # 烂函数，不收敛(而且定义域还小)
    print(sovle_fixed_point(g_c, root, 1e-6, 100, 2))
    print(sovle_fixed_point(g_d, root, 1e-6, 100, 2))
    print(sovle_fixed_point(g_e, root, 1e-6, 100, 2))
