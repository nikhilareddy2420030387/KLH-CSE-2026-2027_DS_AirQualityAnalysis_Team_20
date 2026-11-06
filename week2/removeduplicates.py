#Removing duplicates
import pandas as pd
import numpy as np
#sample dataset wth duplicates
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
print("Original Data:\n",df)
#remove exact duplicates
df_exact = df.drop_duplicates()
print("\nAfter Exact Match Removal:\n",df_exact)