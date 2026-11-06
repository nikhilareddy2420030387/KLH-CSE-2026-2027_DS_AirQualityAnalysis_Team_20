import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = sns.load_dataset('iris')
sns.kdeplot(x=df['petal_length'],
            y=df['petal_width'])
plt.show()