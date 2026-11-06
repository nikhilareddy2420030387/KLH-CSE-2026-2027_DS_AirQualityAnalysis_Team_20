import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

#Scatter plot
plt.figure(figsize=(6,4))
sns.scatterplot(x=df['sepal length (cm)'], y=df['sepal width (cm)'],hue=df['species'])
plt.title("ScatterPlot: Sepal length vs Sepal Width")
plt.show()

#Line Chart(trend of sepal length across samples)
plt.figure(figsize=(6,4))
plt.plot(df['sepal length (cm)'])
plt.title("Line Chart of Sepal Length")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()