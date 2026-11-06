import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

#heatmap(correlation matrix)
plt.figure(figsize=(8,6))
sns.heatmap(df.iloc[:,:4].corr(),annot=True, cmap="coolwarm")
plt.title("Heatmap of feature correlations")
plt.show()

#Bubble chart(scatter with size = petal length)
plt.figure(figsize=(6,4))
plt.scatter(df['sepal length (cm)'],df['sepal width (cm)'],s =df['petal length (cm)']*20,alpha=0.5,c=df['species'])
plt.title("Bubble chart: Sepal vs Petal(size=petal length)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()

#Pairplot(relationships among all features)
sns.pairplot(df.iloc[:,:4])
plt.suptitle("Pair Plot of Iris Feaures",y=1.02)
plt.show()

# Violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(x=df['species'], y=df['sepal length (cm)'])
plt.title("Violin Plot: Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()
