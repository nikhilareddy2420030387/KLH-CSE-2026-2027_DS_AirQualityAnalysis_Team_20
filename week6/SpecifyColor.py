import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"C:\DATA SCIENCE\week5\tips.csv")

sns.countplot(x='sex', data=df, color='skyblue')

plt.show()