import numpy as np
import scipy.linalg

# System 1
A1 = np.array([[1, 1], [2, 1]])
b1 = np.array([17, 10])

x1 = np.linalg.solve(A1, b1)
inv_A1 = np.linalg.inv(A1)
P1, L1, U1 = scipy.linalg.lu(A1)

I_check1 = np.allclose(np.dot(inv_A1, A1), np.eye(A1.shape[0]))
Ax_b_check1 = np.allclose(np.dot(A1, x1), b1)

# System 2
A2 = np.array([[1, 5], [2, 9]])
b2 = np.array([2, 4])

x2 = np.linalg.solve(A2, b2)
inv_A2 = np.linalg.inv(A2)
P2, L2, U2 = scipy.linalg.lu(A2)

I_check2 = np.allclose(np.dot(inv_A2, A2), np.eye(A2.shape[0]))
Ax_b_check2 = np.allclose(np.dot(A2, x2), b2)

# System 3
A3 = np.array([[1, 1, 0], [2, 1, -1], [3, 1, -2]])
b3 = np.array([3, 2, 3])

x3 = np.linalg.solve(A3, b3)
inv_A3 = np.linalg.inv(A3)
P3, L3, U3 = scipy.linalg.lu(A3)

I_check3 = np.allclose(np.dot(inv_A3, A3), np.eye(A3.shape[0]))
Ax_b_check3 = np.allclose(np.dot(A3, x3), b3)

# System 4
A4 = np.array([
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [3, 2, 1, 1],
    [4, 3, 2, 1]
])
b4 = np.array([4, 5, 7, 10])

x4 = np.linalg.solve(A4, b4)
inv_A4 = np.linalg.inv(A4)
P4, L4, U4 = scipy.linalg.lu(A4)

I_check4 = np.allclose(np.dot(inv_A4, A4), np.eye(A4.shape[0]))
Ax_b_check4 = np.allclose(np.dot(A4, x4), b4)

answer = {
    'task_1': {
        'A': A1,
        'b': b1,
        'inv_A': inv_A1,
        'L': L1,
        'U': U1,
        'x': x1,
        'I_check': I_check1,
        'Ax_b_check': Ax_b_check1
    },
    'task_2': {
        'A': A2,
        'b': b2,
        'inv_A': inv_A2,
        'L': L2,
        'U': U2,
        'x': x2,
        'I_check': I_check2,
        'Ax_b_check': Ax_b_check2
    },
    'task_3': {
        'A': A3,
        'b': b3,
        'inv_A': inv_A3,
        'L': L3,
        'U': U3,
        'x': x3,
        'I_check': I_check3,
        'Ax_b_check': Ax_b_check3
    },
    'task_4': {
        'A': A4,
        'b': b4,
        'inv_A': inv_A4,
        'L': L4,
        'U': U4,
        'x': x4,
        'I_check': I_check4,
        'Ax_b_check': Ax_b_check4
    }
}