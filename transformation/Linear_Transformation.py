import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import utils
# import w3_unittest


def T(v):
    w = np.zeros((3, 1))
    w[0, 0] = 3 * v[0, 0]
    w[2, 0] = -2 * v[1, 0]

    return w


v = np.array([[3], [5]])
w = T(v)

print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)
print("\n----------------------------\n")
u = np.array([[1], [-2]])
v = np.array([[2], [4]])
k = 7

print("Original vector 'v':\n", v)
print("With scalar multiplication vector 'v':\n", k*v)
print("\nTransformation of vector 'v':\n", T(v))
print("\nT(k*v):\n", T(k*v), "\n\n k*T(v):\n", k*T(v), "\n\n")

print("\n")
# print("Original vector 'u':\n", u)
# print("Transformation of vector 'u':\n", T(u))

# print("T(u+v):\n", T(u+v), "\n\n T(u)+T(v):\n", T(u)+T(v))

