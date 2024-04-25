from math import sin, pi


def fun_max(f, a, b, linkspace):
    x = a
    max = f(a)
    while x < b:
        x += linkspace
        if f(x) > max:
            max = f(x)
    return max


def fun_min(f, a, b, linkspace):
    x = a
    min = f(a)
    while x < b:
        x += linkspace
        if f(x) < min:
            min = f(x)
    return min


def f(x):
    return sin(x)


fun_max_f = fun_max(f, 0, 2 * pi, 0.01)
fun_min_f = fun_min(f, 0, 2 * pi, 0.01)
print("sin(x)的最大值为：", fun_max_f)
print("sin(x)的最小值为：", fun_min_f)
