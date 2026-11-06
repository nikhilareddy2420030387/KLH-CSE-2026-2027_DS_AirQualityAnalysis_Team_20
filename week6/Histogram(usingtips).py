import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")

plt.hist(data['total_bill'], bins=5, color='skyblue', edgecolor='black')

plt.title("Histogram Example")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

plt.show()