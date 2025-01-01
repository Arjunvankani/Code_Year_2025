
import numpy as np
from sklearn.linear_model import LinearRegression



#Improved Linear Regression with visualization

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare the data
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5]])
y = np.dot(X, np.array([10, 10])) + 5

# Fit the linear regression model
reg = LinearRegression().fit(X, y)

# Make predictions
y_pred = reg.predict(X)

# Evaluate the model
r2 = reg.score(X, y)
print(f"R-squared: {r2}")

# Print model parameters
print(f"Coefficients: {reg.coef_}")
print(f"Intercept: {reg.intercept_}")

# Predict for a new data point
new_data = np.array([[3, 1]])
prediction = reg.predict(new_data)
print(f"Prediction for {new_data}: {prediction}")

# Visualize the results (3D plot)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, c='blue', label='Actual')
ax.scatter(X[:, 0], X[:, 1], y_pred, c='red', label='Predicted')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('y')
ax.set_title('Linear Regression 3D Visualization')
ax.legend()
plt.show()
