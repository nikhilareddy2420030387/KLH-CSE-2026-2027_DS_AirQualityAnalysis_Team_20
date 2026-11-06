import numpy as np
from scipy.linalg import lu

A = np.array([[2, -1, -2],
              [-4, 6, 3],
              [-4, -2, 8]], dtype=float)

b = np.array([-2, 9, -5], dtype=float)

P, L, U = lu(A)

y = np.linalg.solve(L, P @ b)
x = np.linalg.solve(U, y)

print("Matrix A:")
print(A)

print("\nLower Matrix L:")
print(L)

print("\nUpper Matrix U:")
print(U)

print("\nSolution x:")
print(x)