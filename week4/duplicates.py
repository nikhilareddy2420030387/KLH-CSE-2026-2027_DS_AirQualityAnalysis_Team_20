import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df['age'] = df['age'].fillna(df['age'].median())

df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

df.drop_duplicates(inplace=True)

df = pd.get_dummies(
    df,
    columns=['sex', 'embarked', 'class'],
    drop_first=True
)

print(df.head())