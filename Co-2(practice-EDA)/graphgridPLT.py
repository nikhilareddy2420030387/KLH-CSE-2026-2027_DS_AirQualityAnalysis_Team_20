import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\DATA SCIENCE\Co-2(practice-EDA)\temporal.csv")

print(df)

plt.plot(df['Mes'], df['data science'], label='data science')
plt.plot(df['Mes'], df['machine learning'], label='machine learning')
plt.plot(df['Mes'], df['deep learning'], label='deep learning')

plt.xlabel('Date')
plt.ylabel('Popularity')
plt.title('Popularity of AI terms by date')

plt.xlim(0, 20)
plt.ylim(0, 100)

plt.grid(True)
plt.legend()

plt.show()