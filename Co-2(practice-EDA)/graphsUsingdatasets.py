import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\DATA SCIENCE\Co-2(practice-EDA)\temporal.csv")

print(df)

plt.plot(df['deep learning'], df['machine learning'], color='red')

plt.xlabel('deep learning')
plt.ylabel('machine learning')
plt.title('line plot')

plt.show()