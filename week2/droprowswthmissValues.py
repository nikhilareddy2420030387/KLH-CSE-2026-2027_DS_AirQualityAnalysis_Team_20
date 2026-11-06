import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})

# Display Original Dataset
print("Original Dataset (With Missing Values):")
print(df)

# Drop rows with missing values
df_drop = df.copy()
df_drop.dropna(inplace=True)

print("\nDataset After Dropping Rows:")
print(df_drop)