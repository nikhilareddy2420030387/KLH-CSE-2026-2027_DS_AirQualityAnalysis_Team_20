import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45]
})

print("Original Data:")
print(data)

scaler = StandardScaler()

standardized_data = scaler.fit_transform(data)

standardized_data = pd.DataFrame(
    standardized_data,
    columns=data.columns
)

print("\nStandardized Data:")
print(standardized_data)