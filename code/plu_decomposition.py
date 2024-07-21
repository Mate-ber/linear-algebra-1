from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_1 import gauss_elimination_1
import numpy as np


def plu_decomposition(A):
    A = A.astype(float)
    n = A.shape[0]
    identity_matrix = np.eye(n)
    L = np.eye(n)
    
    p, U, identity_matrix = gauss_elimination_1(A, identity_matrix)
    P, u, L = gauss_elimination_1(identity_matrix, L)

    return P, L, U