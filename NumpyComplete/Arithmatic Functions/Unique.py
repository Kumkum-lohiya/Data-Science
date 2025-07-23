import numpy as np
var = np.array([1,2,3,4,2,5,6,2,7])
x = np.unique(var)
print(x)
x1 = np.unique(var,return_index=True)
print(x1)
x2 = np.unique(var,return_counts=True)
print(x2)