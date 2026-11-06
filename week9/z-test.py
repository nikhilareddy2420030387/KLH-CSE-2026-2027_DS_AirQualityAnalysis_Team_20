import numpy as np
from statsmodels.stats.weightstats import ztest

data = np.random.normal(11.8, 0.5, 100)

z, p = ztest(data, value=12)

print("Z-statistic:", z)
print("P-value:", p)