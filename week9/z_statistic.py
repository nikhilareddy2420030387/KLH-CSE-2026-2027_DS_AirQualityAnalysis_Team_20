import numpy as np
from statsmodels.stats.weightstats import ztest

data = np.random.normal(loc=11.8, scale=0.5, size=100)

population_mean = 12
population_std_dev = 0.5

z_statistic, p_value = ztest(data, value=population_mean)

print(f"Z-statistic: {z_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis: The average battery life is different from 12 hours.")
else:
    print("Fail to reject the null hypothesis: The average battery life is not significantly different from 12 hours.")