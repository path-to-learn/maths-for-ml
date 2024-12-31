import numpy as np

a = np.array([[1, -2], [2, 4]])

print("a.shape = ", a.shape)
print("Matrix a is: \n", a)

reflection_on_x_axis = np.array([[1, 0], [0, -1]])
print("Reflection on x-axis: \n", a @ reflection_on_x_axis)


reflection_on_y_axis = np.array([[-1, 0], [0, 1]])
print("Reflection on y-axis: \n", a @ reflection_on_y_axis)