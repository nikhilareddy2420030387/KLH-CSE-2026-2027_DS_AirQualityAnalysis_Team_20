import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1000], [1200], [1500], [1800], [2000]])
y = np.array([50, 55, 65, 80, 90])

model = LinearRegression()
model.fit(X, y)

price = model.predict([[1700]])

print("House Sizes:")
print(X.flatten())

print("\nHouse Prices:")
print(y)

print("\nPredicted Price for 1700 sq.ft:")
print(price[0])