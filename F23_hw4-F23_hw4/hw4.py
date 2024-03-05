import numpy as np

A = np.array([[1, 1, 1],
              [1, 0, 1],
              [0, 1, 1], 
              [2, 1, 1]])
b = np.array([[1],
              [2],
              [1],
              [-1]])

weights = np.linalg.pinv(A.T @ A) @ A.T @ b
print(weights)


A = np.array([[0, 0.5, 1], [2, 0.5, 1]])
b = np.array([[2.5], [0.5]])
print(np.linalg.lstsq(A, b))