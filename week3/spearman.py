import pandas as pd
from scipy.stats import spearmanr

# Exam dataset
df = pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [12, 18, 33, 47, 55]
})

# Spearman correlation coefficient and p-value
corr_value, p_value = spearmanr(df['X'], df['Y'])

print(f"Spearman correlation coefficient: {corr_value}")
print(f"p-value: {p_value}")

