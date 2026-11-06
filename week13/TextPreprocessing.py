import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

# Create dataset
X, y = make_blobs(n_samples=20, centers=3, random_state=42)

# Apply Hierarchical Clustering
linked = linkage(X, method='ward')

# Display dendrogram
dendrogram(linked)

plt.title("Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()