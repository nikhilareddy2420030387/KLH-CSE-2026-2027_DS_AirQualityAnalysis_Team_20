import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})

# Display Original Dataset
print("Original Dataset (With Missing Values):")
print(df)

# Drop cols with missing values
df_drop = df.copy()
df_drop.dropna(axis=1, inplace=True)

print("\nDataset After Dropping Columns:")
print(df_drop)