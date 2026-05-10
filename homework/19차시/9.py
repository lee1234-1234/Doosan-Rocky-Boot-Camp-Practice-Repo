from scipy.optimize import root

def equation(x):
    return (x - 3) ** 2

sol = root(equation, x0=0)

print(f"근: {sol.x}")