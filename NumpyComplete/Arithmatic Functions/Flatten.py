import numpy as np
var = np.array([1,2,3,4,5,6])
y = np.resize(var,(3,2))
print(y)
print()
print(y.flatten())
print(y.flatten(order="F"))
print("Flatten Order :",y.flatten(order= "F"))
print("Ravel :",np.ravel(y,order="K"))