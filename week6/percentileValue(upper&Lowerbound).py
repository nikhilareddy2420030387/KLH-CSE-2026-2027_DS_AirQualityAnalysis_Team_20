import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv('week5/temporal.csv')
df
Q1 = np.percentile(df['data science'],25, method = 'midpoint')
Q3 = np.percentile(df['data science'],75,method='midpoint')
IQR  = Q3-Q1
print("the output of IQR")
print(IQR)

upper = Q3+1.5*IQR
upper_array = np.array(df['data science']>=upper)
print("Upper Bound:",upper)
print(upper_array.sum())
#Lower Bound
lower = Q1-1.5*IQR
lower_array = np.array(df['data science']<=lower)
print("Lower Bound:",lower)
print(lower_array.sum())

