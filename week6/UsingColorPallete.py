import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")

sns.countplot(x='sex',data = df,palette='Set1')
plt.show()