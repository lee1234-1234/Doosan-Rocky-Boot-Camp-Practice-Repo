import numpy as np
import statsmodels.api as sm

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

W = model.params[1]

print("기울기 (coef):", W)