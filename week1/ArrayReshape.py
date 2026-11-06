import numpy as np
n = np.array([1,2,3,4,5,6])
print(n.shape) #6
print(n.reshape(2,3))
print(n.reshape(3,2))
##Reshape from 3D array to 1D array
n.reshape(-1)