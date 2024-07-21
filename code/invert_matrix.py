from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2

import numpy as np

def invert_matrix(A):
    A = A.astype(float)
    n = A.shape[0]
    identity_matrix = np.eye(n)
    tol = 1e-8
    P, U, identity_matrix = gauss_elimination_1(A, identity_matrix)
    
    if np.any(np.abs(np.diag(U)) < tol):
        return None
    
    for i in range(n):
        for j in range(i):
            if np.abs(U[i, j]) > tol:
                return None

    _, inverse_matrix = gauss_elimination_2(U, identity_matrix)
    
    
    dif = np.abs(A.astype(float) @ inverse_matrix - np.eye(A.shape[0])).sum()
    
    # if dif > tol:
    #     return None

    return inverse_matrix