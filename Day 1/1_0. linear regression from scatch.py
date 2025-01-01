import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class LinearRegression_scratch:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1)
        betas = np.linalg.inv(X.T @ X) @ X.T @ y
        self.coef_ = betas[1:]
        self.intercept_ = betas[0]

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return X @ np.concatenate(([self.intercept_], self.coef_))


X = np.random.rand(100, 2)
y = 2*X[:,0] + 3*X[:,1] + np.random.randn(100)

model_sklearn = LinearRegression()
model_sklearn.fit(X,y)

model_scratch = LinearRegression_scratch()
model_scratch.fit(X,y)
y_pred = model_scratch.predict(X)
y_pred_sklearn = model_sklearn.predict(X)
plt.figure(figsize=(8,6))
plt.scatter(y, y_pred, label='From Scratch')
plt.scatter(y, y_pred_sklearn, label='sklearn')
plt.plot(y,y,'r', label='Best fit line')
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.legend()
plt.show()
plt.savefig('actual_vs_predicted_comparison.png')
