from scipy.stats import binom

n = 10
p = 0.7
k = 8

print("Probability of exactly 8 students passing:")
print(binom.pmf(k, n, p))

print("Random Binomial Outcomes:")
print(binom.rvs(n, p, size=5))