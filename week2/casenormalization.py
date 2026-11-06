#sample dataset
import pandas as pd
df = pd.DataFrame({
    'Name':['Alice','BOB','charlie','David']
})
#convert all names to lowercase
df ['Name_lower'] = df['Name'].str.lower()
#convert all names to uppercase
df['Name_upper'] = df['Name'].str.upper()

print("Original Data:")
print(df)

print("\nAfter Case Normalization:")
print(df)