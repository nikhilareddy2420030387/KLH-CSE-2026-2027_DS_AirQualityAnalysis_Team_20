import numpy as np

A = np.array([[4, 2],
              [1, 3]], dtype=float)

values, vectors = np.linalg.eig(A)

print("Original Matrix:")
print(A)

print("\nEigenvalues:")
print(values)

print("\nEigenvectors:")
print(vectors)