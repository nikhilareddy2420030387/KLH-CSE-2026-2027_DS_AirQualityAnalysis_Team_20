import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv('week5/temporal.csv')
df
Q1 = np.percentile(df['data science'],25, method = 'midpoint')
Q3 = np.percentile(df['data science'],75,method='midpoint')
IQR = Q3-Q1
print("the output of IQR")
print(IQR)
