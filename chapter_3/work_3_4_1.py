def sovle_secant(f, x0, x1, toc, nmax, iteration=0):
    while iteration < nmax:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < toc:
            return x2, iteration
        x0 = x1
        x1 = x2
        iteration += 1
    print("迭代次数超过最大值,计算失败")
    return None, None
