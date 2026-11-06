import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = sns.load_dataset("tips")
sns.displot(data['total_bill'],kde=False,color='red',bins=30)
plt.show()