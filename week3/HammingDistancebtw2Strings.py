from scipy.spatial.distance import hamming

A = "101010"
B = "100110"

distance = sum(x != y for x, y in zip(A, B))

print("Binary String 1:", A)
print("Binary String 2:", B)
print("Hamming Distance:", distance)