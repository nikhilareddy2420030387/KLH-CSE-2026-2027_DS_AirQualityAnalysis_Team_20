import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\DATA SCIENCE\week7\tips.csv")

# Heatmap
sns.heatmap(df[["total_bill","tip","size"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Bubble Chart
plt.scatter(df["total_bill"], df["tip"], s=df["size"]*50, alpha=0.5)
plt.title("Bubble Chart")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# Pairplot
sns.pairplot(df[["total_bill","tip","size"]])
plt.show()

# Violin Plot
sns.violinplot(x=df["day"], y=df["total_bill"])
plt.title("Violin Plot")
plt.show()