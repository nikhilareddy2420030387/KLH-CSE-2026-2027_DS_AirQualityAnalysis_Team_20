import scipy.stats as stats

t_statistic = 5.13
df = 10

p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), df))

print("P-value:", p_value)
