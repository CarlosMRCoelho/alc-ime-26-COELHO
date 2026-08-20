import numpy as np
from numpy import linalg

a = np.array([[5,3],[3,2]])
print(a)
print()

a0 = linalg.matrix_power(a, 0)
print(a0)
print()

a3 = linalg.matrix_power(a, 3)
print(a3)
print()

ainv = linalg.inv(a)
print(ainv)