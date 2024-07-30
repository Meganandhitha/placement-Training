import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 2, 3, 5])

model = LinearRegression().fit(X, y)
predictions = model.predict(X)

plt.scatter(X, y, color='black')
plt.plot(X, predictions, color='blue', linewidth=3)
plt.show()
