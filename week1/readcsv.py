import pandas as pd
df = pd.read_csv('iris.csv')
print(df)#prints entire data
print(df.head(10))#prints first few rows and col
print(df.tail(10))#prints last few rows and col
print(df.info())# gives information regarding data
print(df.shape)#gives how many no.of rows and cols are there
