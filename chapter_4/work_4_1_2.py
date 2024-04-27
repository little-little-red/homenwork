def guass_elimination_pivoting(argmented_matrix):
    import numpy as np
    n = argmented_matrix.shape[0]
    for i in range(n):
        # 找列主元
        pivot = i
        for j in range(i + 1, n):
            if np.abs(argmented_matrix[j, i]) > np.abs(argmented_matrix[pivot,
                                                                        i]):
                pivot = j
        argmented_matrix[[i, pivot]] = argmented_matrix[[pivot, i]]
        # 判断列主元是否为0
        if argmented_matrix[i, i] == 0:
            print("no unique solution exists.")
            return None
        # 化上三角矩阵
        for j in range(i + 1, n):
            argmented_matrix[j] = argmented_matrix[j] - argmented_matrix[
                i] * argmented_matrix[j, i] / argmented_matrix[i, i]
        # 求解
        x = np.zeros(n)
        x[n - 1] = argmented_matrix[n - 1, n] / argmented_matrix[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            x[i] = (argmented_matrix[i, n] -
                    np.dot(argmented_matrix[i, i + 1:n],
                           x[i + 1:n])) / argmented_matrix[i, i]
        print("The system of equations has a unique solution:", x)
        return x


if __name__ == "__main__":
    import numpy as np

    # Example usage
    A = np.array([[0.003, 59.14], [5.291, -6.13]])
    b = np.array([59.17, 46.78])
    argmented_matrix = np.column_stack((A, b))
    guass_elimination_pivoting(argmented_matrix)
