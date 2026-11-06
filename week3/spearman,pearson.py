import pandas as pd
from scipy.stats import pearsonr, spearmanr

# Student marks in 5 subjects
df = pd.DataFrame({
    'Maths': [85, 70, 90, 60, 75],
    'Physics': [80, 65, 95, 55, 70],
    'Chemistry': [88, 72, 92, 58, 76],
    'English': [82, 68, 89, 62, 73],
    'Computer': [90, 75, 96, 65, 80]
})

print("Student Marks:")
print(df)

# Pearson correlation
pearson_corr, pearson_p = pearsonr(df['Maths'], df['Physics'])

# Spearman correlation
spearman_corr, spearman_p = spearmanr(df['Maths'], df['Physics'])

print("\nPearson Correlation:", pearson_corr)
print("Pearson p-value:", pearson_p)

print("\nSpearman Correlation:", spearman_corr)
print("Spearman p-value:", spearman_p)