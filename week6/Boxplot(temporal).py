import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('week5/temporal.csv')
df

sns.boxplot(df['data science'])

plt.show()