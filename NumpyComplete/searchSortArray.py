import numpy as np
var1 = np.array([1,2,3,4,6,7,8])
x1 = np.searchsorted(var1,5)
print(x1)

var2= np.array([1,2,3,4,6,7,8,9,10])
x2 = np.searchsorted(var2,8,side="right")
print(x2)