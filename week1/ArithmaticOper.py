import numpy as np
#sum(): adds all elements in array'
n1 = np.array([1,2,3,4])
n2 = np.array([4,5,6,7])
print(np.sum([n1,n2]))
print(np.sum([n1,n2],axis=1))#adds rowwise elem
print(np.sum([n1,n2],axis=0))#adds colwise elem

print(np.subtract(n1,n2))#subtraction
print(np.multiply(n1,n2))#multiplication
print(np.divide(n1,n2))#division