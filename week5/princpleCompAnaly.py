import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

tips = sns.load_dataset("tips")

numeric_cols = tips.select_dtypes(include=['float64', 'int64'])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_cols)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(
    data=pca_result,
    columns=['pc1', 'pc2']
)

print("Explained variance ratio:", pca.explained_variance_ratio_)

print("\nPCA Result: (first 5 rows):")
print(pca_df.head())

# Graph
plt.scatter(pca_df['pc1'], pca_df['pc2'])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA - PC1 vs PC2")
plt.show()
