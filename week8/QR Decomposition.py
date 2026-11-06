import numpy as np

A = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 1]], dtype=float)

b = np.array([4, 5, 6], dtype=float)

Q, R = np.linalg.qr(A)

y = Q.T @ b
x = np.linalg.solve(R, y)

print("Matrix A:")
print(A)

print("\nOrthogonal Matrix Q:")
print(Q)

print("\nUpper Triangular Matrix R:")
print(R)

print("\nSolution x:")
print(x)