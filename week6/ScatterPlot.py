import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"C:\DATA SCIENCE\week5\temporal.csv")
print(df)
plt.scatter(df['deep learning'],df['machine learning'],color = 'red',marker="*")
plt.title ('Scatter Plot')
plt.xlabel('Deep Learning')
plt.ylabel('Machine Learning')
plt.show()
plt.grid()
plt.show()