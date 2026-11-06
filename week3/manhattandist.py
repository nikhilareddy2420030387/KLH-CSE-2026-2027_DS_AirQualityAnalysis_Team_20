import numpy as np
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])
# Manhattan Distance
manhattan_dist = distance.cityblock(pointA, pointB)
print("Manhattan Distance:", manhattan_dist)

# Manhattan Similarity
similarity_manhattan = 1 / (1 + manhattan_dist)
print("Manhattan Similarity:", similarity_manhattan)
manhattan_dist = distance.cityblock(pointA,pointB)
print("Manhattan Distance:",manhattan_dist)

#similarity(inverse of distance)

similarity_manhattan = 1/(1+manhattan_dist)
print("Manhattan Similarity:", similarity_manhattan)