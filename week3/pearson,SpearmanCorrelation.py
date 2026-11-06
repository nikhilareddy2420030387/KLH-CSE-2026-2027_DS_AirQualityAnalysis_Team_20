import pandas as pd

data = {
    'X': [10, 20, 30, 40, 50],
    'Y': [15, 25, 35, 45, 55]
}

df = pd.DataFrame(data)

print("Pearson Correlation:")
print(df['X'].corr(df['Y'], method='pearson'))

print("Spearman Rank Correlation:")
print(df['X'].corr(df['Y'], method='spearman'))