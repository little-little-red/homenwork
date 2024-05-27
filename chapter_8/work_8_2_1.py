def fourth_Runge_kutta(f, y0, t0, t1, h):
    t = [t0]
    y = [y0]
    while t0 + h < t1:
        k1 = f(t0, y0)
        k2 = f(t0 + h / 2, y0 + h / 2 * k1)
        k3 = f(t0 + h / 2, y0 + h / 2 * k2)
        k4 = f(t0 + h, y0 + h * k3)
        y0 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t0 = t0 + h
        t.append(t0)
        y.append(y0)
    return t, y


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    def f(t, y):
        return 2 * t * y

    def exact(t):
        return 4 * np.exp(t**2)

    t, y = fourth_Runge_kutta(f, 4, 0, 1, 0.1)
    plt.plot(t, y)
    t = np.linspace(0, 1, 100)
    plt.plot(t, exact(t))
    plt.show()
