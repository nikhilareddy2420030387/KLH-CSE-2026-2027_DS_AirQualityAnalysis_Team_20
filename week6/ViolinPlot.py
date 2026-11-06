import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("iris")

sns.violinplot(x='species',y='petal_length',data = data)
plt.title("Violin Plot")

plt.show()