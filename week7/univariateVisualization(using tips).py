import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load tips dataset
df = pd.read_csv(r"C:\DATA SCIENCE\week7\tips.csv")

# Histogram
plt.figure(figsize=(6,4))
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(x=df["total_bill"])
plt.title("Boxplot of Total Bill")
plt.xlabel("Total Bill")
plt.show()

# Pie Chart
day_counts = df["day"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(day_counts, labels=day_counts.index, autopct="%1.1f%%")
plt.title("Day Distribution (Pie Chart)")
plt.show()