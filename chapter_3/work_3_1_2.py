from work_3_0_1 import paprmeter_supplementation  # 参数补充装饰器
from work_3_1_1 import solve_BisMethod  # 二分法计算根


def func(x):
    return x**3 + 4 * x**2 - 10


func = paprmeter_supplementation("x")(func)
root, iteration = solve_BisMethod(func, 1, 2, 1e-4, 100)
print(root)
