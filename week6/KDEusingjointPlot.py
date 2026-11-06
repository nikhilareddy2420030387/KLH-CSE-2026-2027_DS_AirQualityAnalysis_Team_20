import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=sns.load_dataset("tips")
sns.jointplot(x='total_bill',y='tip',data = data)
plt.show()