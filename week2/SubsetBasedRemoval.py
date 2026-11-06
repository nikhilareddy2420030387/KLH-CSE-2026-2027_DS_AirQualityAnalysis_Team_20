import pandas as pd
df = pd.DataFrame({
    'ID':[1,2,3,4,4,5,5],
    'Name':['Alice','Bob','Bob','Charlie','David','David','David'],
    'Age' : [25,30,30,35,40,40,40]
})
print("Original Data\n",df)
#removal based on id
df_subset_id = df.drop_duplicates(subset = ['ID'])
print("\nAfter Subset-Based Removal(Id):\n",df_subset_id)
#removal based on name
df_subset_name = df.drop_duplicates(subset = ['Name'])
print("\nAfter Subset-Based Removal(Name):\n",df_subset_name)

