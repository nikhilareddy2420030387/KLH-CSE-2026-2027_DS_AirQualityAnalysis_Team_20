import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]], dtype=float)

U, S, VT = np.linalg.svd(A)

print("Original Matrix:")
print(A)

print("\nMatrix U:")
print(U)

print("\nSingular Values:")
print(S)

print("\nMatrix VT:")
print(VT)

print("\nReconstructed Matrix:")
print(U[:, :2] @ np.diag(S) @ VT)