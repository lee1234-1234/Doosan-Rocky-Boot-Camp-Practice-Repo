import statsmodels.api as sm

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

print(f"절편: {model.params[0]}")
print(f"기울기: {model.params[1]}")