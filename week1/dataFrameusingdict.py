import pandas as pd

# Dictionary as columns (default)
data = {
    'col_1': [3, 2, 1, 0],
    'col_2': ['a', 'b', 'c', 'd']
}

df1 = pd.DataFrame.from_dict(data)
print(df1)

# Dictionary as rows
data = {
    'row_1': [3, 2, 1, 0],
    'row_2': ['a', 'b', 'c', 'd']
}

df2 = pd.DataFrame.from_dict(data, orient='index')
print(df2)