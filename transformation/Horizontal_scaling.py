import numpy as np


def T_hscaling(v):
    A = np.array([[2, 0], [0, 1]])
    w = A @ v
    return w


def transform_vectors(T, v1, v2):
    V = np.hstack((v1, v2))
    W = T(V)
    return W


e1 = np.array([[1], [0]])
e2 = np.array([[0], [1]])

transformation_result_hscaling = transform_vectors(T_hscaling, e1, e2)

print("Original vectors:\n e1= \n", e1, "\n e2=\n", e2,
      "\n\n Result of the transformation (matrix form):\n", transformation_result_hscaling)


def T_reflection_yaxis(v):
    A = np.array([[-1, 0], [0, 1]])
    w = A @ v
    return w


e1 = np.array([[1], [0]])
e2 = np.array([[0], [1]])

transformation_result_reflection_yaxis = transform_vectors(T_reflection_yaxis, e1, e2)

print("Original vectors:\n e1= \n", e1, "\n e2=\n", e2,
      "\n\n Result of the transformation (matrix form):\n", transformation_result_reflection_yaxis)

