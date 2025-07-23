import numpy as np
var = np.array([1,2,3,4])
print(var)
v = np.insert(var,(2,4),(40,50))
a = np.append(var,6.5)
print(v)
print(a)
print(var.dtype)
print(type(var))
print()

#2d array
var1 = np.array([[1,2,3],[1,2,3]])
v1 = np.insert(var1,2, [[22],[23],[24]],axis= 1)
a1 = np.append(var1,[[45,46,47]],axis=0)
print(var1)
print(v1)
print(a1)


# DELETE

var2 = np.array([1,2,3,4])
print(var2)
d = np.delete(var2,2)
print(d)