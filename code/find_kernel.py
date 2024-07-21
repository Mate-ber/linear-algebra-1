from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2

import numpy as np

def find_kernel(A):
    A = A.astype(float)
    n, m = A.shape

    _, U, _ = gauss_elimination_1(A, np.eye(n))
    U, _ =  gauss_elimination_2(A, np.eye(n))


    return B
