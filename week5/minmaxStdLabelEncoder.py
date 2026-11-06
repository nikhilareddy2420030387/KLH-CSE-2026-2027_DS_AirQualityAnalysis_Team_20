import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
import seaborn as sns

tips =sns.load_dataset("tips")

print("Original Data(first 5 rows):")
print(tips.head())

numeric_cols = tips.select_dtypes(include=['float64','int64',]).columns
Scaler_minmax = MinMaxScaler()
tips_normalized = tips.copy()
tips_normalized[numeric_cols] = Scaler_minmax.fit_transform(tips[numeric_cols])
print("\nNormalizedData(first 5 rows):")
print(tips_normalized.head())

scaler_standard = StandardScaler()
tips_standardized =tips.copy()
tips_standardized[numeric_cols] = scaler_standard.fit_transform(tips[numeric_cols])

print("\nStandardizedData (first 5 rows):")
print(tips_standardized.head())

tips_onehot = pd.get_dummies(tips,columns=['sex','smoker','day','time'])
print("\nOneHot")
print(tips_onehot)