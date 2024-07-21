import numpy as np

answer = {
    'task_1': {
        'partial': np.array([[2, 1, 0]]).T,
        'null_space': [np.array([[1, 0, 1]]).T]
    },
    'task_2': {
        'partial': np.array([[6, 8, 0, 0, 0]]).T,
        'null_space': [
            np.array([[-1, -1, 1, 0, 0]]).T,
            np.array([[-1, -1, 0, 1, 0]]).T,
            np.array([[-1, -1, 0, 0, 1]]).T
        ]
    },
    'task_3': {
        'partial': np.array([[3, -11, 5, 0, 0]]).T,
        'null_space': [
            np.array([[-1, 0, -1, 1, 0, 0]]).T,
            np.array([[-2, 0, -1, 0, 1, 0]]).T,
            np.array([[-3, 0, -1, 0, 0, 1]]).T
        ]
    }
}