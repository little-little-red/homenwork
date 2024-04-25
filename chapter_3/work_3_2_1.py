def sovle_fixed_point(f, x0, tol, nmax, limit, iteration=0):
    while iteration < nmax:
        x1 = f(x0)
        if abs(x1) > limit:
            print("超出范围，函数不收敛")
            return None, iteration
        if abs(x1 - x0) < tol:
            return x1, iteration
        x0 = x1
        iteration += 1
    print("迭代次数超过最大值，计算失败")
    return None, iteration
