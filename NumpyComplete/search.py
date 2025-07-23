import numpy as np
var = np.array([4,2,3,4,2,5,2,5,6,7])
print(var)
print()
x = np.where((var%2)== 0)
print(x)