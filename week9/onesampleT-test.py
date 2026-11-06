from scipy.stats import ttest_1samp

data = [65, 70, 75, 80, 68]

t, p = ttest_1samp(data, 70)

print("T-statistic:", t)
print("P-value:", p)