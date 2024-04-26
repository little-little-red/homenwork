def guass_elimination(argmented_matrix):
    import numpy as np
    n = argmented_matrix.shape[1]
    k = 0
    ker = []
    for i in range(n):
        for j in range(k, n):
            if argmented_matrix[i, j] != 0:
                argmented_matrix[[j, k]] = argmented_matrix[[k, j]]
                for m in range(j + 1, n):
                    argmented_matrix[:,
                                     m] = argmented_matrix[:,
                                                           m] - argmented_matrix[:, k] * argmented_matrix[
                                                               i,
                                                               m] / argmented_matrix[
                                                                   i, k]
                k += 1
                ker.append(i)
                break
    for i in range(n - 1, -1, -1):
        if argmented_matrix[ker[-1], i] != 0:
            r_matrix = i + 1
            break
    for i in range(n - 1, -1, -1):
        if argmented_matrix[n, i] != 0:
            r_vector = i + 1
            break
    if r_matrix < r_vector:
        print("向量不在矩阵的列空间中，方程组没有解")
        return None
    elif r_matrix == n:
        x = np.zeros(n)
        x[n - 1] = argmented_matrix[n, n - 1] / argmented_matrix[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            x[i] = (argmented_matrix[n, i] -
                    np.dot(argmented_matrix[i + 1:n, i],
                           x[i + 1:n])) / argmented_matrix[i, i]
        print("这个方程组有唯一解", x)
        return x
    else:
        x = np.zeros(n)
        x[ker[r_matrix -
              1]] = argmented_matrix[n, r_matrix -
                                     1] / argmented_matrix[ker[r_matrix - 1],
                                                           r_matrix - 1]
        for i in ker[r_matrix - 1::-1]:
            x[i] = (argmented_matrix[n, i] -
                    np.dot(argmented_matrix[i + 1:n, i],
                           x[i + 1:n])) / argmented_matrix[i, i]
        print("这个方程组有无穷多解，这里只给出一个解：", x)
        return x


if __name__ == "__main__":
    import numpy as np
    A = [[1, 2, 3, -1], [1, 1, -1, 2], [0, -1, -1, 3], [3, 1, 2, -1]]
    b = [4, 1, -3, 4]
    A_arg = np.vstack((A, b))
    guass_elimination(A_arg)
