from random import random
from time import time

# Matrix multiplication with different loop orderings: 
# 1. i, j, k
# 2. j, k, i
# 3. j, i, k
# 4. k, i, j
# 5. k, j, i
# 6. i, k, j

def multiply_ijk(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):      # i, j, k
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_jki(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for j in range(n):      # j, k, i
        for k in range(n):
            for i in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_jik(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for j in range(n):      # j, i, k
        for i in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_kij(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for k in range(n):      # k, i, j
        for i in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_kji(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for k in range(n):      # k, j, i
        for j in range(n):
            for i in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_ikj(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):      # i, k, j
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def time_multiplication(multiply, A, B):
    start_time = time()
    multiply(A, B)
    end_time = time()
    return end_time - start_time

# Set up
n = 10000  # Size of the matrices: 10,000 x 10,000
A = [[random() for _ in range(n)] for _ in range(n)]
B = [[random() for _ in range(n)] for _ in range(n)]
output = ""
# Output
output += "Timing different loop orderings:\n"
output += f'i, j, k: {time_multiplication(multiply_ijk, A, B)}\n' # 1
output += f'j, k, i: {time_multiplication(multiply_jki, A, B)}\n' # 2
output += f'j, i, k: {time_multiplication(multiply_jik, A, B)}\n' # 3
output += f'k, i, j: {time_multiplication(multiply_kij, A, B)}\n' # 4
output += f'k, j, i: {time_multiplication(multiply_kji, A, B)}\n' # 5
output += f'i, k, j: {time_multiplication(multiply_ikj, A, B)}\n' # 6
# Write results
with open('output.txt', 'w') as fp:
    fp.write(output)