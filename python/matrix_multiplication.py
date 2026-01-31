import numpy as np

# Matrix A - 2x3
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Matrix B - 3x2
matrix_b = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Multiplication using @
result = matrix_a @ matrix_b
print(result)

result_matmul = np.matmul(matrix_a, matrix_b)
print(result_matmul)
