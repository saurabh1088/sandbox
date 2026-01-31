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

# Multiplication using np.dot
result_dot = np.dot(matrix_a, matrix_b)
print(result_dot)

# Invalid multiplication example (uncomment to see the error)
# matrix_c = np.array([
#     [1, 2],
#     [3, 4]
# ])
# invalid_result = matrix_a @ matrix_c  # This will raise a ValueError

# Matrix Transposition
transposed_a = matrix_a.T
print(transposed_a)

# Batch Multiplication
print("Batch Multiplication Example:")
batch_a = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])

batch_b = np.array([
    [[1, 0],
     [0, 1],
     [1, 1]],

    [[2, 1],
     [1, 0],
     [0, 1]]
])

result_batch = batch_a @ batch_b
print(result_batch)

# Real World Examples
print("Real World Example - User-Item Scores:")
# Users × Features
users = np.array([
    [1, 0, 1],
    [0, 1, 1]
])

# Features × Items
items = np.array([
    [5, 2],
    [3, 4],
    [1, 1]
])

scores = users @ items
print(scores)


# TODOs
# Batch matmul
# Linear transformations
# Solving systems
# Broadcasting
# Performance considerations
