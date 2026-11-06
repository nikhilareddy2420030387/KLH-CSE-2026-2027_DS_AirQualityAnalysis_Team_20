from scipy.stats import chi2_contingency

data = [[20, 30],
        [25, 25]]

chi2, p, dof, expected = chi2_contingency(data)

print("Chi-square:", chi2)
print("P-value:", p)
print("degree of freedom",dof)
print("Expected freq:")
print(expected)