
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1,1],[1,2],[1,3],[1,4],[1,5],[2,1],[2,2],[2,3],[2,4],[2,5]])
y = np.dot(X,np.array([10,10]))+5

print(X,y)
reg = LinearRegression().fit(X,y)
print(reg.score(X,y))

print(reg.coef_)
print(reg.intercept_)
print(reg.predict(np.array([[3,1]])))

