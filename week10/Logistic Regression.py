import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[40], [50], [60], [70], [80], [90]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

price = np.array([[75]])

prediction = model.predict(price)
probability = model.predict_proba(price)

print("House Price:", price[0][0])

print("\nPurchase Prediction:")
print(prediction[0])

print("\nPrediction Probability:")
print(probability)