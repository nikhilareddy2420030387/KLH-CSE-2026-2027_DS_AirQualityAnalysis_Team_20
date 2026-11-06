import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Create dataset
X, y = make_blobs(n_samples=100, centers=3, random_state=42)

# Apply K-Means
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

labels = model.labels_
centers = model.cluster_centers_

print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(centers)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200)
plt.title("K-Means Clustering")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()