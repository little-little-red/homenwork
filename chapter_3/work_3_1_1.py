def solve_BisMethod(f,
                    a,
                    b,
                    toc,
                    nmax,
                    iteration=0):  # f是要解的函数，a和b是区间，toc是精确度，nmax是最大迭代次数
    while iteration < nmax:
        p = a + (b - a) / 2
        if f(p) == 0 or (b - a) / 2 < toc:
            return p, iteration
        iteration += 1
        if f(a) * f(p) < 0:
            return solve_BisMethod(f, a, p, toc, nmax, iteration)
        else:
            return solve_BisMethod(f, p, b, toc, nmax, iteration)

    print("迭代次数超过最大值,计算失败")
    return None, iteration
