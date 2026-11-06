import numpy as np
from scipy.spatial.distance import euclidean, cityblock, minkowski

A = np.array([2, 4, 6, 9])
B = np.array([5, 8, 10, 12])

print("Euclidean Distance:", euclidean(A, B))
print("Manhattan Distance:", cityblock(A, B))
print("Minkowski Distance (p=2):", minkowski(A, B, p=2))