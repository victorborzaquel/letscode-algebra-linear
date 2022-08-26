import numpy as np

matriz1 = np.array([[1,0,0,1], [2,2,2,5], [3,4,6,7], [7,4,6,4]])
matriz2 = np.array([[1,0,1,2], [2,2,1,4], [2,4,1,9], [3,4,0,1]])

mul = matriz1 * matriz2
print(mul)

mul_escalar = matriz1 * 3
print(mul_escalar)

mul_dot = np.dot(matriz1, matriz2)
print(mul_dot)