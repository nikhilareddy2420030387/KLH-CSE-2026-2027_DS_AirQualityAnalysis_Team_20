import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("titanic")
sns.histplot(df['age'],bins=20,kde=True)
plt.title("Age Distribution")
plt.show()