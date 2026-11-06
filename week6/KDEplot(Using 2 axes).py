import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
x = np.random.randn(200)
y = np.random.randn(200)
sns.kdeplot(x=x,y=y)
plt.show()