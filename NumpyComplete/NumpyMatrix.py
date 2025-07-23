import numpy as np
# CREATION OF MATRIX
var = np.matrix([[1,2,3],[1,2,3]])
print(var)
print(type(var))
print(var.dtype)
print()

#ARITHMATIC OPERATION IN MATRIX
var1 = np.matrix([[1,2,3],[1,2,3]])
var2 = np.matrix([[1,2,3],[1,2,3]])
print(var1)
print(var2)
print(var1 + var2)
print()

#MATRIX MULTIPLICATION
var3 = np.matrix([[1,2],[1,2]])
var4 = np.matrix([[1,3],[1,3]])
print(var3)
print(var4)
print()
print(var3*var4)
print(var4.dot(var3))
