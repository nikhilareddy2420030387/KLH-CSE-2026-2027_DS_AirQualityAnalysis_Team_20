import numpy as np
from scipy.spatial import distance

pointA = np.array([2,4,6])
pointB = np.array([5,1,9])

#Euclidean Distance
euclidean_dist = distance.euclidean(pointA, pointB)
print("Euclidean Distance:",euclidean_dist)

#similarity(inverse of distance)
similarity_euclidean = 1/(1+euclidean_dist)
print("Euclidean Similarity:",similarity_euclidean)