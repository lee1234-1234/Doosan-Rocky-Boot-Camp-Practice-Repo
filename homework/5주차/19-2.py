from scipy.optimize import root

def equation(x):
    return x**2 + 6*x + 9

sol = root(equation, x0=0)

print(f"근: {sol.x}")