from sklearn.linear_model import LassoCV
from sklearn.datasets import make_regression
X, y = make_regression(noise=4, random_state=0)
reg = LassoCV(cv=5, random_state=0).fit(X, y)
print(reg.score(X, y))
print(reg.predict(X[:1,]))
print(reg.coef_)
print(reg.intercept_)
print(reg.get_params())