import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

#histogram
plt.figure(figsize=(6,4))
sns.histplot(df['sepal length (cm)'], bins = 20, kde = True)
plt.title("Histogram of Sepal Length")
plt.show()

#Box plot
plt.figure(figsize = (6,4))
sns.boxplot (x=df['sepal length (cm)'])
plt.title("Boxplot of Sepal Length")
plt.show()

#pie chart(species distribution)
species_counts = df['species'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(species_counts, labels=iris.target_names,autopct='%1.1f%%')
plt.title("Species Distribution(Pie chart)")
plt.show()