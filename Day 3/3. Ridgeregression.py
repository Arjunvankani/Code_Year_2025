from sklearn.linear_model import Ridge
import numpy as np

n_samples, n_features = 10,5
rng = np.random.RandomState(0)

y = rng.randn(n_samples)
X = rng.randn(n_samples, n_features)
print(X,y)
clf = Ridge(alpha=1.0)
clf.fit(X,y)

print(clf.coef_)
print(clf.intercept_)
print(clf.get_params())
print(clf.predict(X[0:1]))
