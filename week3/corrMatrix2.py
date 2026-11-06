import pandas as pd

df = pd.read_csv("Iris.csv")

print(df.select_dtypes(include=float).corr(method='pearson'))