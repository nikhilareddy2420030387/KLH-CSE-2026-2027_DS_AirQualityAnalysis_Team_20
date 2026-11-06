import pandas as pd

data = {
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue']
}

df = pd.DataFrame(data)

encoded = pd.get_dummies(df)

print(encoded)