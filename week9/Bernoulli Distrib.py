from scipy.stats import bernoulli

p = 0.7

x = bernoulli.rvs(p, size=10)

print("Bernoulli Samples:")
print(x)

print("Probability of Pass:")
print(bernoulli.pmf(1, p))

print("Probability of Fail:")
print(bernoulli.pmf(0, p))