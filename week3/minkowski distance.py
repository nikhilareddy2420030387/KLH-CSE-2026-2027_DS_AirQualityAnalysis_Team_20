import numpy as np
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

# Minkowski Distance
minkowski_dist = distance.minkowski(pointA, pointB, p=3)
print("Minkowski Distance:", minkowski_dist)

# Similarity
similarity_minkowski = 1 / (1 + minkowski_dist)
print("Minkowski Similarity:", similarity_minkowski)