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

def time_multiplication(multiply, A, B, order):    
    start_time = time()
    print(f'Starting {order}: {start_time}')
    multiply(A, B)
    end_time = time()
    print(f'Finished {order}: {end_time}')
    return end_time - start_time

# Set up
n = 1000  # Size of the matrices: 1,000 x 1,000
A = [[random() for _ in range(n)] for _ in range(n)]
B = [[random() for _ in range(n)] for _ in range(n)]
multiplication_methods = {
    "i, j, k": multiply_ijk,
    "j, k, i": multiply_jki,
    "j, i, k": multiply_jik,
    "k, i, j": multiply_kij,
    "k, j, i": multiply_kji,
    "i, k, j": multiply_ikj
}
output = ""
# Run
for order, func in multiplication_methods.items():
    output += f'{order}: {time_multiplication(func, A, B, order)}\n'
# Write results
with open('output.txt', 'w') as fp:
    fp.write(output)