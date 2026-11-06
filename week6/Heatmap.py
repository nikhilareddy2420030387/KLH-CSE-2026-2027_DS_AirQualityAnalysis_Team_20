import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = np.random.randint(1,100,(10,10))
sns.heatmap(data,vmin=30,vmax=70)
plt.show()