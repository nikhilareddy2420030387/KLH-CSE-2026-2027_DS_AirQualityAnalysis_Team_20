#kernalDensityEstimate
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
x  = np.random.randn(200)
y = np.random.randn(200)
sns.kdeplot(x,shade=True)
sns.kdeplot(y)

plt.show()
