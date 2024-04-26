def guass_elimination(argmented_matrix):
    """
    Perform Gaussian elimination on an augmented matrix to solve a system of linear equations.

    Args:
        argmented_matrix (numpy.ndarray): The augmented matrix representing the system of linear equations.

    Returns:
        numpy.ndarray or None: The solution vector if the system has a unique solution, None otherwise.
    """
    import numpy as np

    n = argmented_matrix.shape[1]  # Number of columns in the augmented matrix
    k = 0  # Pivot row index
    ker = []  # List to store the indices of pivot rows

    # Perform Gaussian elimination
    for i in range(n):
        for j in range(k, n):
            if argmented_matrix[i, j] != 0:
                # Swap columns to make the pivot element non-zero
                argmented_matrix[:, [j, k]] = argmented_matrix[:, [k, j]]

                # Perform row operations to eliminate elements below the pivot
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

    r_matrix = len(ker)  # Rank of the matrix

    # Find the rank of the augmented matrix
    for i in range(n - 1, -1, -1):
        if argmented_matrix[n, i] != 0:
            r_vector = i + 1
            break

    # Check the number of solutions
    if r_matrix < r_vector:
        print(
            "The vector is not in the column space of the matrix. The system of equations has no solution."
        )
        return None
    elif r_matrix == n:
        # Solve for a unique solution
        x = np.zeros(n)
        x[n - 1] = argmented_matrix[n, n - 1] / argmented_matrix[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            x[i] = (argmented_matrix[n, i] -
                    np.dot(argmented_matrix[i + 1:n, i],
                           x[i + 1:n])) / argmented_matrix[i, i]
        print("The system of equations has a unique solution:", x)
        return x
    else:
        # Solve for a particular solution
        x = np.zeros(n)
        x[ker[r_matrix -
              1]] = argmented_matrix[n, r_matrix -
                                     1] / argmented_matrix[ker[r_matrix - 1],
                                                           r_matrix - 1]
        for i in ker[r_matrix - 1::-1]:
            x[i] = (argmented_matrix[n, i] -
                    np.dot(argmented_matrix[i + 1:n, i],
                           x[i + 1:n])) / argmented_matrix[i, i]
        print(
            "The system of equations has infinitely many solutions. Here is one particular solution:",
            x)
        return x


if __name__ == "__main__":
    import numpy as np

    # Example usage
    A = [[1, 2, 3, -1], [1, 1, -1, 2], [0, -1, -1, 3], [3, 1, 2, -1]]
    b = [4, 1, -3, 4]
    A_arg = np.vstack((A, b))
    guass_elimination(A_arg)
