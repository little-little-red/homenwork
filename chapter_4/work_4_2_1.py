def tridiag_matrix_solver(a, b, c, d):
    n = len(d)
    a = [0] + a
    x = [0] * n
    c[0] = c[0] / b[0]
    d[0] = d[0] / b[0]
    for i in range(1, n - 1):
        c[i] = c[i] / (b[i] - a[i] * c[i - 1])
    for i in range(1, n):
        d[i] = (d[i] - a[i] * d[i - 1]) / (b[i] - a[i] * c[i - 1])
    x[n - 1] = d[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = d[i] - c[i] * x[i + 1]
    print("The solution is:", x)
    return x


if __name__ == "__main__":

    # Example usage
    a = [2, 3]
    b = [1, 2, 3]
    c = [2, 3]
    d = [1, 2, 3]
    tridiag_matrix_solver(a, b, c, d)
