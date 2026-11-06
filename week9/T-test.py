from scipy.stats import ttest_1samp

data = [65, 70, 75, 80, 68]

test = ttest_1samp(data, 70)

print(test)