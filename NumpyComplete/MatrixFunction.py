import numpy as np
# TRANSPOSSE OF  MATRIX
var = np.matrix([[1,2,3],[4,5,6]])
print(var)
print()
print(np.transpose(var))
print(var.T)
print()

#SWAPAXES
print(np.swapaxes(var,0,1))
var1 = np.matrix([[1,2],[3,4]])
print(var1)
print()
print(np.swapaxes(var1,0,1))

#INVERSE
var2 = np.matrix([[1,2],[3,4]])
print(var2)
print()
print(np.linalg.inv(var2))

#POWER
var3 = np.matrix([[1,2],[3,4]])
print(var3)
print()
print(np.linalg.matrix_power(var3,2))
print(np.linalg.matrix_power(var3,0))
print(np.linalg.matrix_power(var3,-2))

#DETERMINANT
var4 = np.matrix([[1,2,3],[3,4,5],[1,2,3]])
print(var4)
print()
print(np.linalg.det(var4))