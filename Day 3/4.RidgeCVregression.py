from sklearn.linear_model import  RidgeCV
from sklearn.datasets import load_diabetes

X,y = load_diabetes(return_X_y=True)

clf = RidgeCV(alphas=[1e-3,1e-2,1e-1,1]).fit(X,y)
print(clf.score(X,y))
