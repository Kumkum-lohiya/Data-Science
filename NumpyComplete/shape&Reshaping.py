import numpy as np

var = np.array([[1,2,3,4],[1,2,3,4]])
print(var)
print()
print(var.shape)

var1 = np.array([1,2,3,4],ndmin = 4)
print(var1)
print(var1.ndim)
print(var1.shape)
print()
#Reshaping array
var2 = np.array([1,2,3,4,5,6])
print(var2)
print(var2.ndim)
x = var2.reshape(3,2)
print(x)


var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var2)
print(var2.ndim)
x1 = var3.reshape(2,3,2)
print(x1)

x2 = x1.reshape(-1)
print(x2)