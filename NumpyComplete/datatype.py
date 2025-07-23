import numpy as np
var = np.array([1,2,3,4,12,13,14,15])
print("Data Type :",var.dtype)

var1 = np.array([1.0,1.1,1.2,1.3])
print("Data Type :",var1.dtype)

#To change the datatype

x = np.array([1,2,3,4],dtype=np.int8)
print(x.dtype)


x1 = np.array([1,2,3,4],dtype="f")
print(x1.dtype)

#data type as a function

x2 = np.array([1,2,3,4])
new = np.float32(x2)
print("Data Type :",x2.dtype)
print("Data Type :",new.dtype)

x3 = np.array([1,2,3,4])
new_1 = x3.astype(float)
print(x3)
print(new_1)



