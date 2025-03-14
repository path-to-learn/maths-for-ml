# This format of module import allows to use the sympy functions without sympy. prefix.
from sympy import symbols, pprint, sqrt
import numpy as np

# This is actually sympy.sqrt function, but sympy. prefix is omitted.
print(sqrt(18))

def differential(x):
    return sqrt(x)

x_array = np.array([18])
print(x_array)
print(differential(18))

# List of symbols.
x, y = symbols('x y')
# Definition of the expression.
expr = 2 * x**3 - x * y
## print(expr)
pprint(expr)

## Get the derivative
def getDerivative(exp):
    return exp.diff(x)

print(getDerivative(expr))

