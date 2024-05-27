def numerical_diff_two_point(f, x, h):
    return (f(x + h) - f(x)) / h


def numerical_diff_three_point_right(f, x, h):
    return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)


def numerical_diff_three_point_mid(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


if __name__ == '__main__':
    import numpy as np

    def f(x):
        return np.log(x)

    x0 = 1.8
    h = np.linspace(0.01, 0.1, 10)

    df_2p = numerical_diff_two_point(f, x0, h)
    df_3pr = numerical_diff_three_point_right(f, x0, h)
    df_3pm = numerical_diff_three_point_mid(f, x0, h)
    print(f'df_2p: {df_2p} df_3pr: {df_3pr}, df_3pm: {df_3pm}')
