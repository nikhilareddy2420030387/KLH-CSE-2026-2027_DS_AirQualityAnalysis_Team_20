import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\DATA SCIENCE\week7\tips.csv")

# Scatter Plot
plt.figure(figsize=(6,4))

sns.scatterplot(
    x=df["total_bill"],
    y=df["tip"],
    hue=df["sex"]
)

plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# Line Chart
plt.figure(figsize=(6,4))

plt.plot(df["total_bill"], label="Total Bill")
plt.plot(df["tip"], label="Tip")

plt.title("Line Chart of Total Bill and Tip")
plt.xlabel("Sample Index")
plt.ylabel("Amount")
plt.legend()
plt.show()