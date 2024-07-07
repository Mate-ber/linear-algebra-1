import numpy as np


N = 100

A = np.diag([i for i in range(1, N + 1)])
B = np.diag([i for i in range(1, N + 1)])

for i in range(N):
    for j in range(i+1, N):
        A[i][j] = 1
        B[i][j] = 1

result = (A.T) @ B

answer = {
    'task': result
}