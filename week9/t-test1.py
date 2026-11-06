from scipy.stats import ttest_ind

data1 = [65, 70, 75, 80, 68]
data2 = [72, 74, 78, 82, 76]

t, p = ttest_ind(data1, data2)

print("T-statistic:", t)
print("P-value:", p)