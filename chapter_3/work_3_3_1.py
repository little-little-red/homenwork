from scipy.misc import derivative


def sovle_newton(f, x0, toc, nmax, iteration=0):
    while iteration < nmax:
        x1 = x0 - f(x0) / derivative(f, x0, dx=1e-6)
        if abs(x1 - x0) < toc:
            return x1, iteration
        x0 = x1
        iteration += 1
    print("迭代次数超过最大值,计算失败")
    return None, None
