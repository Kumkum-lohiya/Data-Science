import numpy as np
#COPY
var = np.array([1,2,3,4])
co = var.copy()
var[1] = 40
co[2] = 50
print("var :",var)
print("copy :",co)
print()

#VIEW
x = np.array([1,2,3,4])
vi = x.view()
x[1] = 40
vi[2] = 50
print("var :",x)
print("view :",vi)
print()
