from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2

import numpy as np

def find_kernel(A):
    ## YOUR CODE HERE
    A = A.astype(float)
    n, m = A.shape

    # Step 1: Perform Gaussian Elimination Stage 1
    _, U, _ = gauss_elimination_1(A, np.eye(n))
    U, _ =  gauss_elimination_2(A, np.eye(n))

    # Step 2: Identify columns of U corresponding to free variables (non-pivotal columns)
    null_space_basis = []
    pivots = []
    for j in range(m):
        if j < n and U[j, j] == 0:
            null_vector = np.zeros(m)
            null_vector[j] = 1.0  # Setting the free variable to 1
            for i in range(j):
                if U[i, j] != 0:
                    null_vector[i] = -U[i, j]
            null_space_basis.append(null_vector)
        else:
            pivots.append(j)

    # Step 3: Construct the null space matrix B
    B = np.array(null_space_basis).T

    return B
