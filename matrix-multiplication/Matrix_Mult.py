import numpy as np

x = np.array([1, -2, -5])
y = np.array([4, 3, -1])
print("y.shap = ", y.shape)
try:
    print("Matrix Multiplication using matmul :", np.matmul(x, y))
    print("Matrix Multiplication using @operator :", x @ y)
except ValueError as err:
    print(err)

x = np.array([[1, -2, -5], [1, 2, 3]])
print("x.shap = ", x.shape)
try:
    print("Matrix Multiplication :", np.matmul(x, y))
    print("Matrix Multiplication :", x @ y)
except ValueError as err:
    print(err)