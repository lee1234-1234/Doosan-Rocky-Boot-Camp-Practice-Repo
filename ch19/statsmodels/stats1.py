# stats1.py

import statsmodels.api as sm

data = sm.datasets.get_rdataset("mtcars").data
print(data.head())
# print(data)
X = data['hp']
y = data['mpg']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
# ols = sm.OLS().fit()
# 같은거
# ols = sm.OLS()
# ols.fit()
print(model.summary())


print("모델 계수---------")
print(model.params)
print(model.params["hp"])
print(model.params["const"])