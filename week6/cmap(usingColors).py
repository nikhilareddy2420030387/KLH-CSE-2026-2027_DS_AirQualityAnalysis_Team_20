import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('week5/tips.csv')

corr = df.select_dtypes("number").corr()

sns.heatmap(corr, annot=True)

plt.show()