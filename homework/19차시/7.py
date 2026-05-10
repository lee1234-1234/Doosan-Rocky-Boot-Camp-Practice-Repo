import statsmodels.api as sm
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()

predicted_y = model.predict(X)

plt.scatter(x, y)
plt.plot(x, predicted_y, color="Red")

plt.title("Linear Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.show()