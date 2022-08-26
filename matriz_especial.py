import numpy as np

a = np.array([[1,2], [6,7]])
print(a)
print()

# Transposta
t = a.transpose()
print(t)
print()

t = a.T
print(t)
print()

# Identidade
id = np.eye(3)
print(id)
print()

# Inversa ( A.A**-1 = 1 )
b = np.array([[0,1], [3,0]])
print(b)
print()

b_inv = np.linalg.inv(b)
print(b_inv)
print()