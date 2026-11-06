import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data  = sns.load_dataset("tips")
sns.countplot(x ='sex',hue= 'smoker',data = data)
plt.show()