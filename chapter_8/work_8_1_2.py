from work_8_1_1 import euler


def better_euler(f, y0, t0, t1, h):
    t, y = euler(f, y0, t0, t1, h)
    for i in range(len(t) - 1):
        y_mid = y[i] + h * f(t[i], y[i])
        y[i + 1] = y[i] + h / 2 * (f(t[i], y[i]) + f(t[i + 1], y_mid))
    y[-1] = y[-2] + h * f(t[-2], y[-2])
    return t, y


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    def f(t, y):
        return 2 * t * y

    def exact(t):
        return 4 * np.exp(t**2)

    t, y = better_euler(f, 4, 0, 1, 0.1)
    plt.plot(t, y)
    t = np.linspace(0, 1, 100)
    plt.plot(t, exact(t))
    plt.show()
